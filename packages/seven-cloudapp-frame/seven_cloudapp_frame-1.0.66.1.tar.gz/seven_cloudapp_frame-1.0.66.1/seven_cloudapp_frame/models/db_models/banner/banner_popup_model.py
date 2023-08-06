
#此文件由rigger自动生成
from seven_framework.mysql import MySQLHelper
from seven_framework.base_model import *


class BannerPopupModel(BaseModel):
    def __init__(self, db_connect_key='db_middler_platform', sub_table=None, db_transaction=None, context=None):
        super(BannerPopupModel, self).__init__(BannerPopup, sub_table)
        self.db = MySQLHelper(config.get_value(db_connect_key))
        self.db_connect_key = db_connect_key
        self.db_transaction = db_transaction
        self.db.context = context

    #方法扩展请继承此类
    
class BannerPopup:

    def __init__(self):
        super(BannerPopup, self).__init__()
        self.id = 0  # id
        self.popup_name = ""  # 弹窗名称
        self.style_type = 0  # 弹窗样式(0未选择1一般样式2案例样式)
        self.tab_type = 0  # Tab层级(0未选择1一级2二级)
        self.is_show_contact = 0  # 是否展示联系方式(1是0否)
        self.content_title = ""  # 内容标题(如:精彩案例、商业合作等)
        self.popup_desc = ""  # 文案
        self.popup_pic = ""  # 弹窗图
        self.sort_index = 0  # 排序
        self.is_release = 0  # 是否发布(1是0否)
        self.release_date = "1900-01-01 00:00:00"  # 发布时间
        self.create_date = "1900-01-01 00:00:00"  # 创建时间
        self.modify_date = "1900-01-01 00:00:00"  # 更新时间

    @classmethod
    def get_field_list(self):
        return ['id', 'popup_name', 'style_type', 'tab_type', 'is_show_contact', 'content_title', 'popup_desc', 'popup_pic', 'sort_index', 'is_release', 'release_date', 'create_date', 'modify_date']
        
    @classmethod
    def get_primary_key(self):
        return "id"

    def __str__(self):
        return "banner_popup_tb"
    