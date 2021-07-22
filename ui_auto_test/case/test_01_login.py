# 1.导包
import logging
import time
import unittest

from parameterized import parameterized

from config import BASE_PATH
from page.home_page import HomeProxy
from page.login_page import LoginProxy
from utils import DriverUtils, get_msg, build_testData

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


# 2.定义测试类
class TestLogin(unittest.TestCase):  # 固定继承unittest.TestCase；类名可以自己定义

    # 类级别的初始化fixture
    @classmethod  # 固定写法，类级别装饰器
    def setUpClass(cls):  # 固定写法，类级别fixture初始化方法
        # 通过工具类中的方法来获取浏览器驱动对象
        cls.driver = DriverUtils.get_driver()  # cls.driver 自定义实例属性， DriverUtils.get_driver() 自己提前编写好的测试类和方法
        # 在代码开始执行的位置放置所有的创建的驱动的操作
        cls.login_proxy = LoginProxy()
        # 实例化首页业务层对象
        cls.home_proxy = HomeProxy()

    # 类级别的销毁fixture
    @classmethod  # 固定写法，类级别装饰器
    def tearDownClass(cls):  # 固定写法，类级别fixture销毁方法
        # 7.关闭浏览器
        DriverUtils.quit_driver()  # DriverUtils.quit_driver() 自己提前编写好的测试类和方法

    # 方法级别的fixutre
    def setUp(self):  # 固定写法，方法级别初始化装饰器
        self.driver.get("http://localhost/")  # 根据setUpClass方法中所自定义实例属性self.driver(浏览器驱动对象)调用打开网址方法
        # 4.在首页点击登陆操作连接
        # self.driver.find_element_by_css_selector(".red").click()  # 通过调用自己定义的表示浏览器驱动对象的实例属性self.driver调用固定定位方法，并点击
        self.home_proxy.to_login_page()

    # 3.定义测试方法
    # build_testData调用工具中封装好读取数据方法
    @parameterized.expand(build_testData(BASE_PATH + "/data/test_login.json"))
    def test_login(self, username, password, code, expect, is_suc):
        """
        :param username: 用户名
        :param password: 密码
        :param code: 验证码
        :param expect: 期望结果
        :return:
        """
        logging.info("---------------->执行登陆用例")
        self.login_proxy.test_login(username, password, code)
        # 通过判断is_suc标识来决定走正向的断言还是反向断言
        # 正向测试数据放在整个测试数据的最后
        if is_suc:
            logging.info("断言正向结果")
            time.sleep(5)
            msg = self.driver.title
            logging.info(self.assertIn(expect, msg))
        else:
            # 6.打印异常提示框信息
            msg = get_msg()
            # 断言
            logging.info("断言正向结果")
            self.assertIn(expect, msg)
