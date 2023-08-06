# -*- coding: utf-8 -*-
"""
:Author: HuangJianYi
:Date: 2023-04-19 11:37:25
@LastEditTime: 2023-04-19 11:37:05
@LastEditors: HuangJianYi
:Description: 中台相关接口
"""
from enum import Enum, unique
from seven_cloudapp_frame.handlers.frame_base import *
from seven_cloudapp_frame.models.db_models.banner.banner_place_model import *
from seven_cloudapp_frame.models.db_models.banner.banner_content_model import *
from seven_cloudapp_frame.models.db_models.banner.banner_popup_model import *
from seven_cloudapp_frame.models.db_models.banner.banner_style_model import *
from seven_cloudapp_frame.models.db_models.dict.dict_info_banner_model import *


class GetTopBannerListHandler(ClientBaseHandler):
    """
    :description: 后台顶部banner
    """
    def get_async(self):
        """
        :description: 后台顶部banner
        :last_editors: HuangJianYi
        """
        banner_place_model = BannerPlaceModel(context=self)
        banner_content_model = BannerContentModel(context=self)
        product_id = int(config.get_value("project_name",0))
        banner_place_dict_list = banner_place_model.get_dict_list("product_id=%s and is_release=1",order_by="sort_index asc",params=[product_id])
        if len(banner_place_dict_list)>0:
            banner_place_id_list = [i["id"] for i in banner_place_dict_list]
            banner_place_id_condition = SevenHelper.get_condition_by_int_list("place_id",banner_place_id_list)
            banner_content_dict_list = banner_content_model.get_dict_list(f"{banner_place_id_condition} and is_release=1",order_by="sort_index desc")
            if len(banner_content_dict_list)>0:
                for banner_place_dict in banner_place_dict_list:
                    banner_place_dict["content"] = query(banner_content_dict_list).where(lambda x:x["place_id"]==banner_place_dict["id"]).to_list()
        return self.response_json_success(banner_place_dict_list)

class GetBannerPopupHandler(ClientBaseHandler):
    """
    :description: 弹窗内容
    """
    def get_async(self):
        """
        :description: 弹窗内容
        :param popup_id：弹窗id
        :return: list
        :last_editors: HuangJianYi
        """
        popup_id = self.get_param_int("popup_id",0)
        banner_popup_model = BannerPopupModel(context=self)
        banner_style_model = BannerStyleModel(context=self)

        banner_popup = banner_popup_model.get_dict("id=%s and is_release=1",params=[popup_id])
        if not banner_popup:
            return self.response_json_error("error","找不到该弹窗")

        if banner_popup["style_type"] == StyleType.common.value:
            banner_style_dict_list = banner_style_model.get_dict_list("popup_id=%s and is_release=1",order_by="sort_index desc",params=[popup_id])
            tab_list = [tab for tab in banner_style_dict_list if tab["parent_id"]==0]
            tab_list = self.get_child_tab_list(tab_list,banner_style_dict_list)
            banner_popup["tab_list"] = tab_list

        if banner_popup["style_type"] == StyleType.case.value:
            product_id_list = banner_style_model.get_dict_list("popup_id=%s and is_release=1",group_by="product_id",order_by="sort_index desc ",field="product_id",params=[popup_id])
            if len(product_id_list)>0:
                product_id_list = [i["product_id"] for i in product_id_list ]
            trade_id_list = banner_style_model.get_dict_list("popup_id=%s and is_release=1",group_by="trade_id",order_by="sort_index desc",field="trade_id",params=[popup_id])
            if len(trade_id_list)>0:
                trade_id_list = [i["trade_id"] for i in trade_id_list ]

            product_list = []
            dict_info_banner_model = DictInfoBannerModel(context=self)
            if len(product_id_list)>0:
                condition = SevenHelper.get_condition_by_int_list("id",product_id_list)
                product_list = dict_info_banner_model.get_dict_list(f"{condition} and is_release = 1",order_by="sort_index desc")

            trade_list = []
            if len(trade_id_list)>0:
                condition = SevenHelper.get_condition_by_int_list("id",trade_id_list)
                trade_list = dict_info_banner_model.get_dict_list(f"{condition} and is_release = 1",order_by="sort_index desc")

            banner_popup["product_list"] = product_list
            banner_popup["trade_list"] = trade_list

        return self.response_json_success(banner_popup)

    def get_child_tab_list(self,tab_list,all_tab_list):
        if len(tab_list)>0 and len(all_tab_list)>0:
            for parent_tab in tab_list:
                parent_tab["child_tab_list"] = [child_tab for child_tab in all_tab_list if child_tab["parent_id"]==parent_tab["id"]]
                if len(parent_tab["child_tab_list"])>0:
                    parent_tab["child_tab_list"] = self.get_child_tab_list(parent_tab["child_tab_list"],all_tab_list)
        return tab_list

class GetCaseListHandler(ClientBaseHandler):
    """
    :description: 获取案例列表
    """
    def get_async(self):
        """
        :description: 获取案例列表
        :param popup_id：弹窗id
        :param product_id：产品分类id
        :param trade_id：trade_id
        :param page_index：页数
        :param page_size：条数
        :return
        :last_editors: HuangJianYi
        """
        popup_id = self.get_param_int("popup_id",0)
        product_id = self.get_param_int("product_id",0)
        trade_id = self.get_param_int("trade_id",0)
        page_index= self.get_param_int("page_index",0)
        page_size = self.get_param_int("page_size",10)

        condition_where = ConditionWhere()
        condition_where.add_condition("popup_id=%s and is_release=1")
        params=[popup_id]
        if product_id > 0:
            condition_where.add_condition("product_id=%s")
            params.append(product_id)
        if trade_id > 0:
            condition_where.add_condition("trade_id=%s")
            params.append(trade_id)

        banner_style_model = BannerStyleModel(context=self)
        banner_style_dict_list, total = banner_style_model.get_dict_page_list("*", page_index, page_size, condition_where.to_string(), order_by="create_date desc", params=params)
        if len(banner_style_dict_list)>0:
            for index in range(0,len(banner_style_dict_list)):
                if index == 0:
                    banner_style_dict_list[index]["is_show_new"] = 1
                else:
                    banner_style_dict_list[index]["is_show_new"] = 0

        page_info = PageInfo(page_index,page_size,total,banner_style_dict_list)

        return self.response_json_success(page_info)

class StyleType(Enum):
    common = 1 #一般样式
    case = 2 #案例样式