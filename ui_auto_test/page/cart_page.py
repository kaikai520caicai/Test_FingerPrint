"购物车页面-三层封装方式"
import logging

from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


# 对象库层
class CartPage(BasePage):

    def __init__(self):
        super().__init__()
        # 1.定义要操作的元素的实例属性
        # 全选复选框
        self.check_all = (By.CSS_SELECTOR, ".checkCartAll")
        # 去结算超链接
        self.to_settle = (By.CSS_SELECTOR, ".gwc-qjs")

    # 2.定义找到元素的方法
    # 找单选框的元素对象
    def find_check_all(self):
        return self.find_elt(self.check_all)

    # 找去结算的超链接
    def find_to_settle(self):
        return self.find_elt(self.to_settle)


# 操作层
class CartHandle(BaseHandle):

    def __init__(self):
        # 创建对象库层的对象
        self.cart_page = CartPage()

    # 判断勾选框是否勾选，如果勾选上了则不点击，如果未勾选状态则点击勾选
    def click_check(self):
        # 如果未勾选则点击单选框
        if self.cart_page.find_check_all().is_selected() is False:
            self.cart_page.find_check_all().click()

    # 点击去结算的超链接
    def click_to_settle(self):
        self.cart_page.find_to_settle().click()


# 业务层
class CartProxy:

    def __init__(self):
        # 创建操作层的对象
        self.cart_handle = CartHandle()

    # 去提交订单页面
    def to_submit_page(self):
        # 1.勾选全选单选框
        self.cart_handle.click_check()
        # 2.点击去结算
        self.cart_handle.click_to_settle()
