"""
商品搜索结果页
"""
from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


# 对象库层
class SgPage(BasePage):

    # 定义初始化方法
    def __init__(self):
        # 重写初始化方法
        super().__init__()
        # 定义要操作的元素对象的实例属性
        # 加入购物车的超链接（进入详情）
        self.to_gi_link = (By.XPATH, "//*[text()='加入购物车']")

    # 定义找到元素的实例方法
    def find_gi_link(self):
        return self.find_elt(self.to_gi_link)


# 操作层
class SgHandle(BaseHandle):

    def __init__(self):
        self.sg_page = SgPage()

    # 加入购物车去详情的点击
    def click_gi_link(self):
        self.sg_page.find_gi_link().click()


# 业务层
class SgProxy:

    def __init__(self):
        self.sg_handle = SgHandle()

    # 去购物车页面
    def to_info_page(self):
        # 点击加入购物车连接
        self.sg_handle.click_gi_link()
