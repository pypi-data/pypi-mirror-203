
#此文件由rigger自动生成
from seven_framework.mysql import MySQLHelper
from seven_framework.base_model import *


class BannerStyleModel(BaseModel):
    def __init__(self, db_connect_key='db_middler_platform', sub_table=None, db_transaction=None, context=None):
        super(BannerStyleModel, self).__init__(BannerStyle, sub_table)
        self.db = MySQLHelper(config.get_value(db_connect_key))
        self.db_connect_key = db_connect_key
        self.db_transaction = db_transaction
        self.db.context = context

    #方法扩展请继承此类
    
class BannerStyle:

    def __init__(self):
        super(BannerStyle, self).__init__()
        self.id = 0  # id
        self.popup_id = 0  # 弹窗id(banner_popup_tb的主键id)
        self.parent_id = 0  # 父id(上级banner_tab_tb的id)
        self.tab_name = ""  # Tab名称
        self.content_title = ""  # 内容标题
        self.is_show_new = 0  # 是否展示New标签(1是0否)
        self.content_pic = ""  # 内容图片
        self.product_id = 0  # 产品分类id(dict_info_banner_tb的id)
        self.trade_id = 0  # 行业分类id(dict_info_banner_tb的id)
        self.link_url = ""  # 跳转地址
        self.sort_index = 0  # 排序
        self.is_release = 0  # 是否发布(1是0否)
        self.release_date = "1900-01-01 00:00:00"  # 发布时间
        self.create_date = "1900-01-01 00:00:00"  # 创建时间
        self.modify_date = "1900-01-01 00:00:00"  # 更新时间

    @classmethod
    def get_field_list(self):
        return ['id', 'popup_id', 'parent_id', 'tab_name', 'content_title', 'is_show_new', 'content_pic', 'product_id', 'trade_id', 'link_url', 'sort_index', 'is_release', 'release_date', 'create_date', 'modify_date']
        
    @classmethod
    def get_primary_key(self):
        return "id"

    def __str__(self):
        return "banner_style_tb"
    