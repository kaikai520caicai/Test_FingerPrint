"提交订单"
from selenium.webdriver.common.by import By
from base.base_page import BasePage, wait

"""
1.将整个页面当成一个类
2.将所有要操作的元素当成类的实例属性
3.将页面操作方法当成类的实例方法

---在小型的公司需要快速实现自动化情况下可以采用这种模式
"""


class SubOPage(BasePage):

    def __init__(self):
        super().__init__()
        # 2.将所有要操作的元素当成类的实例属性
        # 提交订单按钮
        self.submit_order_btn = (By.CSS_SELECTOR, ".Sub-orders")
        # 提交订单结果信息
        self.submit_order_result = (By.CSS_SELECTOR, ".erhuh h3")
        # 收货地址
        self.recive_address = (By.XPATH, "//*[text()='寄送至']")

    # 将页面操作方法当成类的实例方法
    def test_submit_order(self):
        # WebDriverWait(self.driver, 10, 0.5).until(lambda x: x.find_element(*self.recive_address))
        wait(self.recive_address)
        # 1.点击提交订单
        self.find_elt(self.submit_order_btn).click()
        # 2.获取提交订单的结果并且返回
        return self.find_elt(self.submit_order_result).text
