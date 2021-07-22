"""订单管理页面"""
import time
from selenium.webdriver.common.by import By
from base.base_page import BasePage, to_swtich


# 1.定义代表页面类
class OrderPage(BasePage):

    # 2.定义页面上所需要操作的元素对象的实例属性
    def __init__(self):
        super().__init__()
        # 待付款tab连接
        self.wait_pay_link = (By.CSS_SELECTOR, "#navitems5 [href*='WAITPAY']")
        # 立即支付
        self.hurry_pay_link = (By.CSS_SELECTOR, ".ps_lj")

    # 3.定义测试用例来组织页面上所要提供的业务方法
    # 点击立即支付跳转确认支付方式的业务方法
    def to_order_pay_page(self):
        # 窗口切换
        # handles = self.driver.window_handles
        # self.driver.switch_to.window(handles[-1])
        to_swtich()
        # a.点击待付款tab页面
        time.sleep(3)
        self.find_elt(self.wait_pay_link).click()
        # b.点击第一个确认支付按钮
        self.find_elt(self.hurry_pay_link).click()
