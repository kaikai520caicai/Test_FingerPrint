"""
商品详情页
"""
import time

"""
商品搜索结果页
"""
from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


# 对象库层
class GiPage(BasePage):

    # 定义初始化方法
    def __init__(self):
        # 重写初始化方法
        super().__init__()
        # 定义要操作的元素对象的实例属性
        # 购物车按钮
        self.add_btn = (By.ID, "join_cart")
        # iframe元素
        self.iframe = (By.CSS_SELECTOR, "[id*='layui-layer-i']")
        # 结果元素
        self.add_result = (By.CSS_SELECTOR, ".conect-title span")

    # 找到购物车按钮
    def find_add_btn(self):
        return self.find_elt(self.add_btn)

    # 找结果元素
    def find_add_result(self):
        # iframe切换
        # driver.switch_to.frame(driver.find_element_by_id("2222"))
        self.driver.switch_to.frame(self.find_elt(self.iframe))
        time.sleep(3)
        # 返回加入购物车的元素对象
        return self.find_elt(self.add_result)


# 操作层
class GiHandle(BaseHandle):

    def __init__(self):
        self.gi_page = GiPage()

    # 点击加入购物车
    def click_add_btn(self):
        self.gi_page.find_add_btn().click()

    # 获取加入购物车结果
    def get_add_result(self):
        time.sleep(2)
        msg = self.gi_page.find_add_result().text
        return msg


# 业务层
class GiProxy:

    def __init__(self):
        self.gi_handle = GiHandle()

    # 加入购物车的业务方法
    def test_add_goods(self):
        # 1.点击加入购物车
        self.gi_handle.click_add_btn()
        # 2.获取加入购物车结果
        return self.gi_handle.get_add_result()
