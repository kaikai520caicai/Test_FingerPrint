# 1.导包
import logging
import unittest

from page.cart_page import CartProxy
from page.home_page import HomeProxy
from page.submit_order_page import SubOPage
from utils import DriverUtils


# 2.定义测试类
class TestSubmitOrder(unittest.TestCase):

    # a.定义类级别的初始化方法打开浏览器
    @classmethod
    def setUpClass(cls):
        cls.driver = DriverUtils.get_driver()
        # b.在类级别的方法中需要创建好对应要使用的业务层类的对象
        cls.home_proxy = HomeProxy()
        cls.cart_proxy = CartProxy()
        cls.subo_page = SubOPage()

    # c.在方法级别的初始化fixture执行恢复原点
    def setUp(self):
        self.driver.get("http://localhost/")

    # 3.定义测试方法
    def test_submit_order(self):
        # d.连续调用多个业务层的实例方法，组织成完整文案测试用例的操作步骤
        logging.info("-------->执行提交订单测试用例")
        # 1)在首页点击我的购物车
        self.home_proxy.to_cart_page()
        # 2)在购物车页面点击去结算
        self.cart_proxy.to_submit_page()
        # 3)在提交订单页面点击提交单获取提交结果
        msg = self.subo_page.test_submit_order()
        # e.进行断言
        self.assertIn("订单提交成功", msg)

    # f.定义类级别的销毁的fixture,关闭浏览器
    @classmethod
    def tearDownClass(cls):
        DriverUtils.quit_driver()
