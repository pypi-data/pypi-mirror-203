from django.db import transaction
from django.views.decorators.http import require_http_methods
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from xj_thread.services.thread_category_service import ThreadCategoryService
from xj_thread.services.thread_item_service import ThreadItemService
from xj_thread.services.thread_list_service import ThreadListService
from xj_user.services.user_detail_info_service import DetailInfoService
from xj_user.utils.user_wrapper import user_authentication_force_wrapper, user_authentication_wrapper
from ..service.clock_service import ClockService
from ..service.enroll_record_serivce import EnrollRecordServices
from ..service.enroll_services import EnrollServices
from ..service.enroll_subitem_record_service import EnrollSubitemRecordService
from ..service.rule_service import RuleValueService
from ..service.subitem_service import SubitemService
from ..utils.custom_response import util_response
from ..utils.custom_tool import parse_data, format_params_handle, request_params_wrapper, filter_result_field, flow_service_wrapper, write_to_log
from ..utils.join_list import JoinList


class EnrollAPI(APIView):
    @staticmethod
    def list_handle(*args, request_params=None, user_info=None, **kwargs, ):
        """
        接口执行手柄
        :param request_params: request请求的参数
        :param user_info: 请求的用户信息
        :return: data,err
        """
        # 信息id列表反查询报名
        thread_ids, err = ThreadListService.search_ids(search_prams=format_params_handle(
            param_dict=request_params,
            filter_filed_list=["title", "subtitle", "access_level", "author"],
            is_remove_empty=True
        ))
        if thread_ids:
            request_params["thread_id_list"] = thread_ids

        # 根据平台编码获取类别ID列表
        platform_code = request_params.pop("platform_code", None)
        if platform_code:
            id_list, err = ThreadCategoryService.list(
                filter_fields_params={"platform_code": platform_code},
                filter_fields="id",
                need_pagination=False
            )
            request_params["category_id_list"] = [i["id"] for i in id_list]

        # 报名列表搜索
        data, err = EnrollServices.enroll_list(params=request_params)
        if err:
            return None, err

        # 合并信息表数据
        id_list = [i['thread_id'] for i in data['list'] if i]
        thread_list, err = ThreadListService.search(id_list)
        data['list'] = JoinList(data['list'], thread_list, "thread_id", "id").join()
        # 用户信息合并
        user_id_list = [i['user_id'] for i in data['list'] if i]
        user_info_list = DetailInfoService.get_list_detail(user_id_list=user_id_list, filter_fields=["user_id", "real_name", "full_name", "nickname"])
        data['list'] = JoinList(data['list'], user_info_list, "user_id", "user_id").join()

        # 小数点四舍五入
        for i in data['list']:
            i["price"] = round(i["price"], 2)

        # 结果集字段过滤 TODO 此处应该给默认的 字段列表
        filter_fields = request_params.get("filter_fields", None)
        filter_fields = filter_fields.split(";") if filter_fields else None
        data["list"] = filter_result_field(result_list=data["list"], filter_filed_list=filter_fields)
        # 数据返回
        if err:
            return None, err
        return data, None

    @api_view(['GET'])
    @request_params_wrapper
    @user_authentication_wrapper
    def list(self, *args, request_params=None, user_info=None, **kwargs, ):
        data, err = EnrollAPI.list_handle(request_params=request_params, user_info=user_info, )
        # 数据返回
        if err:
            return util_response(err=1001, msg=err)
        return util_response(data=data)

    @api_view(['POST', ])
    @user_authentication_force_wrapper
    @request_params_wrapper
    @flow_service_wrapper
    def add(self, *args, user_info, request_params, **kwargs, ):
        params = request_params
        # ============   字段验证处理 start ============
        user_id = user_info.get("user_id")
        params.setdefault("user_id", user_id)  # 用户ID

        params.setdefault("subitems", [])  # 报名分项
        enroll_subitem_status_code = params.pop("enroll_subitem_status_code", 242)  # 报名分项 状态码

        # ============ 如果有计价id，并且需要重新计价，补全补全的参数  start ============
        # try:
        #     is_valuate = int(params.pop("is_valuate", 1))  # 是否重新验单，进行计价，补全没有传的参数
        # except Exception:
        #     is_valuate = 0

        # if is_valuate and main_params.get("enroll_rule_group_id"):
        #     print("params:", params)
        # ============ 如果有计价id，并且需要重新计价，补全补全的参数  end ============

        # 信息表参数
        thread_params = format_params_handle(
            param_dict=params,
            remove_filed_list=[
                # 报名表字段
                "trading_relate", "region_code", "occupy_room", "enroll_status_code", "min_number", "max_number", "min_count_apiece", "max_count_apiece",
                "enroll_rule_group", "price", "count", "unit", "fee", "reduction", "subitems_amount", "amount", "paid_amount", "unpaid_amount", "commision",
                "deposit", "hide_price", "hide_user", "has_repeat", "has_subitem", "has_audit", "need_vouch", "need_deposit", "need_imprest", "enable_pool",
                "pool_limit", "pool_stopwatch", "open_time", "close_time", "launch_time", "finish_time", "spend_time", "create_time",
                "update_time", "snapshot", "remark", "finance_invoicing_code",
                # 报名分项字段
                "subitem"
            ],
            alias_dict={"thread_remark": "remark"}
        )
        if not thread_params:
            return util_response(err=1001, msg="请填写项目基本信息")
        thread_params["has_enroll"] = 1  # 默认参数开启报名
        # 报名主表参数
        main_params = format_params_handle(
            param_dict=params,
            filter_filed_list=[
                "thread_id", "user_id", "category_id", "trading_relate", "region_code", "occupy_room", "enroll_status_code", "min_number", "max_number",
                "min_count_apiece", "max_count_apiece", "enroll_rule_group", "enroll_rule_group_id", "price", "count", "unit", "fee", "reduction", "subitems_amount",
                "amount", "paid_amount", "unpaid_amount", "commision", "deposit", "hide_price", "hide_user", "has_repeat", "has_subitem", "has_audit",
                "need_vouch", "need_deposit", "need_imprest", "enable_pool", "pool_limit", "pool_stopwatch", "open_time", "close_time", "launch_time",
                "finish_time", "spend_time", "create_time", "update_time", "snapshot", "remark", "finance_invoicing_code",
            ],
        )
        if thread_params:
            main_params.setdefault("snapshot", thread_params)  # 因为信息表需要调用服务，所以存一组信息表的快照
        # ============   字段验证处理 end ============

        # ============   绑定计价分组ID start ============
        try:
            if not main_params.get("enroll_rule_group_id"):
                # 得到 enroll_rule_group_id
                category_id = thread_params.get("category_id", None)
                classify_id = thread_params.get("classify_id", None)
                if not category_id or not classify_id:
                    raise Exception("category_id，classify_id必填")
                res, err = RuleValueService.group_list({"category_id": category_id, "classify_id": classify_id})
                if err:
                    raise Exception(err)
                if not res:
                    raise Exception("没有找到对应的计价规则组ID")
                main_params.setdefault("enroll_rule_group_id", res[0].get("id"))
        except Exception as e:
            write_to_log(prefix="报名发布，绑定计价组ID异常", err_obj=e)
        # ============   绑定计价分组ID end ============

        # ============ 信息表添加  start ============
        sid = transaction.savepoint()
        thread_id = thread_params.get("thread_id")
        if not thread_id:
            data, err = ThreadItemService.add(thread_params)
        else:
            data, err = ThreadItemService.edit(thread_params, thread_id)
        if err:
            transaction.savepoint_rollback(sid)
            return util_response(err=1002, msg="信息添加错误：" + err)
        # ============ 信息表添加  end   ============

        # ============ 报名主表添加  start ============
        thread_id = thread_id or data['id']
        main_params.setdefault("thread_id", thread_id or data['id'])
        main_params.setdefault("enroll_status_code", 242)
        main_instance, err = EnrollServices.enroll_add(main_params)
        if err:
            transaction.savepoint_rollback(sid)
            return util_response(err=1003, msg=err)
        # ============ 报名主表添加  end ============

        # ============ 报名分项添加  start ============
        for item_params in params.get("subitems", []):
            item_params.setdefault("enroll_id", main_instance.get('id'))
            item_params.setdefault("enroll_subitem_status_code", enroll_subitem_status_code)
            data, err = SubitemService.add(item_params)
            if err:
                transaction.savepoint_rollback(sid)
                return util_response(err=1004, msg=err)
        # ============ 报名分项添加  end ============

        transaction.clean_savepoints()  # 清除保存点
        return util_response(data=main_instance)

    @api_view(['GET', 'POST', ])
    @user_authentication_force_wrapper
    @request_params_wrapper
    def detail(self, *args, user_info=None, request_params=None, **kwargs, ):
        # 参数验证
        if request_params is None:
            request_params = {}
        if user_info is None:
            user_info = {}

        params = request_params
        default_remove_fields = [
            "real_name", "sex", "birth", "tags", "signature", "avatar", "cover", "language", "more",
            "id_card_front", "id_card_back", "real_name_is_pass", "id_card",
            "certificate", "work experience", "qualification_certificate", "audit_status",
            "score", "user_name", "phone", "email", "register_time",
            "user_info", "wechat_openid", "is_deleted",
        ]
        filter_fields = params.pop("filter_fields", None)
        remove_fields = params.pop("remove_fields", default_remove_fields)

        enroll_id = kwargs.get("enroll_id", None) or params.pop("enroll_id", None)
        if not enroll_id:
            return util_response(err=1000, msg="参数错误:enroll_id不可以为空")

        user_id = user_info.get("user_id", None)

        # 获取用户详情
        data, err = EnrollServices.enroll_detail(enroll_id, user_id=user_id)
        if err:
            return util_response(err=1001, msg=err)

        # 用户数据拼接
        push_user_info, user_err = DetailInfoService.get_detail(user_id=user_id)
        if push_user_info:
            data.update(push_user_info)

        # 信息表 数据拼接
        thread_list, err = ThreadListService.search([data.get("thread_id")])
        if err:
            return util_response(err=1002, msg=err)
        data = JoinList([data], thread_list, "thread_id", "id").join()
        data = data[0] if not len(data) > 1 else data
        data["price"] = round(data["price"] or 0, 2)

        # 字段过滤
        filter_fields = filter_fields.split(";") if filter_fields and isinstance(filter_fields, str) else filter_fields
        remove_fields = remove_fields.split(";") if remove_fields and isinstance(remove_fields, str) else remove_fields
        data = format_params_handle(data, filter_filed_list=filter_fields, remove_filed_list=remove_fields, is_remove_null=False)
        # 响应数据
        if err:
            return util_response(err=1003, msg=err)
        return util_response(data=data)

    @require_http_methods(['GET'])
    @request_params_wrapper
    @user_authentication_force_wrapper
    def own_list(self, *args, request_params=None, user_info=None, **kwargs):
        # 信息表
        thread_params = format_params_handle(
            param_dict=request_params,
            filter_filed_list=[
                "user_id", "title", "subtitle", "summary", "access_level", "author", "has_enroll", "has_fee", "has_comment", "has_location", "is_original",
            ]
        )
        if thread_params:
            thread_ids, err = ThreadListService.search_ids(thread_params)
            request_params["thread_id_list"] = thread_ids if not err else []

        filter_fields = request_params.pop("filter_fields", None)
        request_params["user_id"] = user_info.get("user_id")
        need_pagination = request_params.pop("need_pagination", 1)
        need_pagination = int(need_pagination)
        data, err = EnrollServices.enroll_own_list(request_params, need_pagination=need_pagination)
        if err:
            return util_response(err=1000, msg=err)
        # 合并thread模块数据
        id_list = [i['thread_id'] for i in data['list'] if i]
        thread_list, err = ThreadListService.search(id_list)
        data['list'] = JoinList(data['list'], thread_list, "thread_id", "id").join()

        filter_fields = filter_fields.split(";") if filter_fields else None
        data["list"] = filter_result_field(result_list=data["list"], filter_filed_list=filter_fields)
        # 数据返回
        if err:
            return util_response(err=1001, msg=err)
        return util_response(data=data)

    @api_view(['GET', 'POST', ])
    @request_params_wrapper
    @user_authentication_force_wrapper
    def undertake_list(self, *args, request_params=None, user_info=None, **kwargs):
        """个人承办列表, 表示的报名记录列表"""
        filter_fields = request_params.get("filter_fields", None)
        request_params["user_id"] = user_info.get("user_id")
        need_pagination = request_params.pop("need_pagination", 1)
        need_pagination = int(need_pagination)
        # 信息表
        thread_params = format_params_handle(
            param_dict=request_params,
            filter_filed_list=[
                "title", "subtitle", "access_level", "author", "has_enroll", "has_fee", "has_comment",
                "has_location", "is_original",
            ]
        )
        if thread_params:
            thread_ids, err = ThreadListService.search_ids(thread_params)
            request_params["thread_id_list"] = thread_ids if not err else []
        data, err = EnrollServices.enroll_undertake_list(request_params, need_pagination=need_pagination)
        if err:
            return util_response(err=1000, msg=err)
        # 分页数据
        if need_pagination:
            for i in data["list"]:
                i['price'] = round(float(i["price"]), 2)
                i['main_amount'] = round(float(i["main_amount"]), 2)
                i['coupon_amount'] = round(float(i["coupon_amount"]), 2)
                i['again_reduction'] = round(float(i["again_reduction"]), 2)
                i['subitems_amount'] = round(float(i["subitems_amount"]), 2)
                i['deposit_amount'] = round(float(i["deposit_amount"]), 2)
                i['amount'] = round(float(i["amount"]), 2)
                i['paid_amount'] = round(float(i["paid_amount"]), 2)
                i['unpaid_amount'] = round(float(i["unpaid_amount"]), 2)
                i['fee'] = round(float(i["fee"]), 2)

            # 合并thread模块数据
            id_list = [i['thread_id'] for i in data['list'] if i]
            thread_list, err = ThreadListService.search(id_list)
            data['list'] = JoinList(data['list'], thread_list, "thread_id", "id").join()

            filter_fields = filter_fields.split(";") if filter_fields else None
            data["list"] = filter_result_field(result_list=data["list"], filter_filed_list=filter_fields)
            # 数据返回
            if err:
                return util_response(err=1001, msg=err)
            return util_response(data=data)
        else:
            for i in data:
                i['price'] = round(float(i["price"]), 2)
                i['main_amount'] = round(float(i["main_amount"]), 2)
                i['coupon_amount'] = round(float(i["coupon_amount"]), 2)
                i['again_reduction'] = round(float(i["again_reduction"]), 2)
                i['subitems_amount'] = round(float(i["subitems_amount"]), 2)
                i['deposit_amount'] = round(float(i["deposit_amount"]), 2)
                i['amount'] = round(float(i["amount"]), 2)
                i['paid_amount'] = round(float(i["paid_amount"]), 2)
                i['unpaid_amount'] = round(float(i["unpaid_amount"]), 2)
                i['fee'] = round(float(i["fee"]), 2)

            # 合并thread模块数据
            id_list = [i['thread_id'] for i in data if i]
            thread_list, err = ThreadListService.search(id_list)
            data = JoinList(data, thread_list, "thread_id", "id").join()

            filter_fields = filter_fields.split(";") if filter_fields else None
            data = filter_result_field(result_list=data, filter_filed_list=filter_fields)
            # 数据返回
            if err:
                return util_response(err=1001, msg=err)
            return util_response(data=data)

    @api_view(['POST', 'PUT'])
    @request_params_wrapper
    @flow_service_wrapper
    def edit(self, *args, request_params=None, **kwargs, ):
        # 参数处理
        if request_params is None:
            request_params = {}
        params = request_params.copy()
        enroll_id = kwargs.get("enroll_id") or params.pop("enroll_id") or None
        if not enroll_id:
            return util_response(err=1000, msg="参数错误:enroll_id不可以为空")
        thread_params = format_params_handle(
            param_dict=params,
            remove_filed_list=[
                "trading_relate", "user_id", "region_code", "occupy_room", "enroll_status_code", "min_number", "max_number",
                "min_count_apiece", "max_count_apiece", "enroll_rule_group", "price", "count", "unit", "fee", "reduction", "subitems_amount", "amount",
                "paid_amount", "unpaid_amount", "commision", "deposit", "hide_price", "hide_user", "has_repeat", "has_subitem", "has_audit", "need_vouch",
                "need_deposit", "need_imprest", "enable_pool", "pool_limit", "pool_stopwatch", "open_time", "close_time", "launch_time", "finish_time",
                "spend_time", "create_time", "update_time", "snapshot", "remark", "finance_invoicing_code"
            ],
            alias_dict={"thread_remark": "remark"}
        )

        main_params = format_params_handle(
            param_dict=params,
            filter_filed_list=[
                "thread_id", "category_id", "trading_relate", "region_code", "occupy_room", "enroll_status_code", "min_number", "max_number",
                "min_count_apiece", "max_count_apiece", "enroll_rule_group", "price", "count", "unit", "fee", "reduction", "subitems_amount", "amount",
                "paid_amount", "unpaid_amount", "commision", "deposit", "hide_price", "hide_user", "has_repeat", "has_subitem", "has_audit", "need_vouch",
                "need_deposit", "need_imprest", "enable_pool", "pool_limit", "pool_stopwatch", "open_time", "close_time", "launch_time", "finish_time",
                "spend_time", "create_time", "update_time", "snapshot", "remark",
            ]
        )
        if thread_params:
            main_params.setdefault("snapshot", thread_params)  # 因为信息表需要调用服务，所以存一组信息表的快照

        # 报名主表修改
        # print("main_params:", main_params)
        instance, err = EnrollServices.enroll_edit(main_params, enroll_id)
        if err:
            return util_response(err=1001, msg=err)

        # 信息表修改
        thread_id = params.pop("thread_id", None) or instance.get("thread_id", None)
        if thread_id and thread_params:
            data, err = ThreadItemService.edit(thread_params, thread_id)
            if err:
                return util_response(err=1002, msg=err)

        # 联动分项数量修改
        subitem__count = params.pop("subitem__count", None)
        if subitem__count:
            data, err = SubitemService.batch_edit({"count": subitem__count}, enroll_id=enroll_id)
            if err:
                return util_response(err=1003, msg=err)

        return util_response(data=instance)

    @require_http_methods(['DELETE'])
    def delete(self, *args, **kwargs, ):
        params = parse_data(self)
        enroll_id = kwargs.get("enroll_id") or params.pop("enroll_id") or None
        if not enroll_id:
            return util_response(err=1000, msg="参数错误:enroll_id不可以为空")
        data, err = EnrollServices.enroll_delete(enroll_id)
        if err:
            return util_response(err=1000, msg=err)
        return util_response(data=data)

    @api_view(['POST', 'PUT'])
    @request_params_wrapper
    @user_authentication_wrapper
    def enroll(self, *args, request_params=None, user_info=None, **kwargs):
        sid = transaction.savepoint()
        # 用户id获取
        request_params.setdefault("user_id", user_info.get("user_id", None))
        if not request_params.get("user_id"):
            return util_response(err=1000, msg="user_id 必填")
        # is_can_add = EnrollRecordServices.check_can_add(enroll_id=request_params.get("enroll_id"), user_id=user_info.get("user_id"))
        # if not is_can_add:
        #     return util_response(err=1001, msg="无法继续报名，当前人数已满")

        # 信息主表
        main_record_params = format_params_handle(
            param_dict=request_params,
            filter_filed_list=[
                "id", "enroll_id", "user_id", "enroll_auth_status_id", "enroll_pay_status_id", "enroll_status_code", "create_time", "price", "deposit", "count",
                "main_amount", "coupon_amount", "again_reduction", "subitems_amount", "deposit_amount", "amount", "paid_amount", "unpaid_amount", "fee", "photos",
                "files", "score", "reply", "remark",
            ]
        )
        main_data, err = EnrollRecordServices.record_add(main_record_params)
        if err:
            transaction.savepoint_rollback(sid)
            return util_response(err=1001, msg=err)

        # 分项表
        subitem_params = format_params_handle(
            param_dict=request_params,
            filter_filed_list=["enroll_record_id", "enroll_subitem_id", "user_id", "subitem_price", "subitem_count", "subitem_amount", ],
            alias_dict={"subitem_price": "price", "subitem_count": "count"}
        )

        enroll_record_id = main_data.get("id", None)
        if not enroll_record_id:
            transaction.savepoint_rollback(sid)
            return util_response(err=1002, msg=err)
        subitem_params["enroll_record_id"] = enroll_record_id

        subitem_data, err = EnrollSubitemRecordService.add(subitem_params)
        if err:
            transaction.savepoint_rollback(sid)
            return util_response(err=1003, msg=err)

        transaction.clean_savepoints()
        # 添加定时器
        clocker = ClockService()
        clocker.add_clock(enroll_id=request_params.get("enroll_id"), user_id=request_params.get("user_id"))
        return util_response()

    @api_view(['DELETE'])
    @request_params_wrapper
    @user_authentication_wrapper
    def un_enroll(self, *args, request_params=None, user_info=None, **kwargs):
        # 用户id获取
        user_id = request_params.get("user_id") or user_info.get("user_id")
        enroll_id = request_params.get("enroll_id")
        if not user_id or not enroll_id:
            return util_response(err=1000, msg="参数错误")

        data, err = EnrollRecordServices.record_del(None, {"user_id": user_id, "enroll_id": enroll_id})

        return util_response()

    @api_view(['GET'])
    @request_params_wrapper
    def enroll_pay_callback(self, *args, request_params=None, **kwargs):
        # 用户id获取
        order_no = request_params.get("order_no", None)
        if not order_no:
            return util_response(err=1000, msg="order_no 不能为空")

        data, err = EnrollServices.bxtx_pay_call_back(order_no)
        if err:
            return util_response(err=1001, msg=err)
        return util_response(msg="回调成功")
