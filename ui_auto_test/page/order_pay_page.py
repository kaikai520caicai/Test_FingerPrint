"""
订单支付页面
"""
from selenium.webdriver.common.by import By
from base.base_page import BasePage, to_swtich, wait


# 1.定义测试类
class OpPage(BasePage):

    # 2.定义页面上所有要操作的元素对象的实例属性
    def __init__(self):
        super().__init__()
        # 付款方式
        self.pay_method = (By.CSS_SELECTOR, "[value*='=cod']")
        # 确认支付方式
        self.con_pay = (By.CSS_SELECTOR, ".button-confirm-payment")
        # 支付结果元素
        self.pay_result = (By.CSS_SELECTOR, ".erhuh h3")

    # 3.定义业务方法
    def test_pay(self):
        # 进入订单支付页面，窗口切换
        to_swtich()
        # 选择货到付款
        wait(self.pay_method).click()
        # 点击确认支付方式
        self.find_elt(self.con_pay).click()
        # 获取支付结果
        return self.find_elt(self.pay_result).text
