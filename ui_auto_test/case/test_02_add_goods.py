import logging
import unittest

from BeautifulReport import BeautifulReport
from parameterized import parameterized

from config import BASE_PATH
from page.goods_info_page import GiProxy
from page.home_page import HomeProxy
from page.search_goods_page import SgProxy
from utils import DriverUtils, build_testData

"""
测试用例：
1.定义测试类，记得继承unittest.TestCase
2.定义类级别的初始化方法
3.在类级别的初始化方法中定义一个cls.driver实例属性，用来创建的获取浏览器驱动对象
4.在类级别的初始化方法中定义对应业务层的实例属性，要完成一个完整的测试用例步骤，可能需要调用多个PO业务层中的业务方法，才能
形成一个完整测试操作步骤。
5.定义类级别的销毁的方法，调用工具类中关闭浏览器驱动的方法
6.定义测试方法，按手工测试步骤才执行(调用)对应PO业务层中的业务方法，通过初始化方法中定义好实例属性来进行方法调用
7.设计断言
8.在data目录定义json格式的测试数据
9.引入参数化，针对测试方法进行调整，@parameterized.expand方法来调用工具文件中读取数据文件方法来获取测试数据
10.修改测试方法参数，测试数据有多少个定义多少个参数，同时修改输入数据地方，使用参数来进行代替
"""


class TestAddGoods(unittest.TestCase):

    # save_img是固定的方法
    def save_img(self, img_name):  # 错误截图方法，这个必须先定义好
        self.driver.get_screenshot_as_file('{}/{}.png'.format(BASE_PATH + "/img", img_name))

    @classmethod
    def setUpClass(cls):
        """
        类级别的初始化fixture在测试类运行开始之前只会运行一次
        """
        # 1.打开浏览器# 2.最大化窗口和隐式等待
        cls.driver = DriverUtils.get_driver()
        # 实例化首页的业务层对象
        cls.home_proxy = HomeProxy()
        # 实例化搜索结果页的业务层对象
        cls.sg_proxy = SgProxy()
        # 实例化商品详情页的业务层对象
        cls.gi_proxy = GiProxy()

    @classmethod
    def tearDownClass(cls):
        """
        类级别的销毁的fixture在整个测试类运行完成之后自动运行一次
        """
        DriverUtils.quit_driver()

    def setUp(self):
        """
        方法级别的初始化fixture在每个测试方法运行之前都会自动运行一次
        """
        self.driver.get("http://localhost/")

    # 固定的装饰器，add_test_img方法的参数必须和方法名一致
    @parameterized.expand(build_testData(BASE_PATH + "/data/test_add_cart.json"))
    @BeautifulReport.add_test_img("test_add_cart")
    def test_add_cart(self, goods_name):
        logging.info("------------->开始执行加入购物车的测试用例")
        # 4.在首页输入搜索关键和点击搜索
        self.home_proxy.search_goods(goods_name)
        # 5.在搜索结果页点击第一个商品进入详情页
        self.sg_proxy.to_info_page()
        # 6.在详情页点击加入购物车并获取加入结果
        msg = self.gi_proxy.test_add_goods()
        # 7.断言
        self.assertIn("添加成功", msg)
