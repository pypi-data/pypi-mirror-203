
#此文件由rigger自动生成
from seven_framework.mysql import MySQLHelper
from seven_framework.base_model import *


class BannerContentModel(BaseModel):
    def __init__(self, db_connect_key='db_middler_platform', sub_table=None, db_transaction=None, context=None):
        super(BannerContentModel, self).__init__(BannerContent, sub_table)
        self.db = MySQLHelper(config.get_value(db_connect_key))
        self.db_connect_key = db_connect_key
        self.db_transaction = db_transaction
        self.db.context = context

    #方法扩展请继承此类
    
class BannerContent:

    def __init__(self):
        super(BannerContent, self).__init__()
        self.id = 0  # id
        self.place_id = 0  # 入口位置id(banner_place_tb的主键id)
        self.entry_name = ""  # 入口名称
        self.is_show_new = 0  # 是否展示New标签(1是0否)
        self.corner_tag_id = 0  # 右上角标签
        self.content_pic = ""  # 内容图片
        self.bottom_desc = ""  # 底部文案
        self.popup_id = 0  # 弹窗id(banner_popup_tb的主键id)
        self.sort_index = 0  # 排序
        self.is_release = 0  # 是否发布(1是0否)
        self.release_date = "1900-01-01 00:00:00"  # 发布时间
        self.create_date = "1900-01-01 00:00:00"  # 创建时间
        self.modify_date = "1900-01-01 00:00:00"  # 更新时间

    @classmethod
    def get_field_list(self):
        return ['id', 'place_id', 'entry_name', 'is_show_new', 'corner_tag_id', 'content_pic', 'bottom_desc', 'popup_id', 'sort_index', 'is_release', 'release_date', 'create_date', 'modify_date']
        
    @classmethod
    def get_primary_key(self):
        return "id"

    def __str__(self):
        return "banner_content_tb"
    