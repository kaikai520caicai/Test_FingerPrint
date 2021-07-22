# 需求：对TPshop项目进行前台登录设计脚本
# 要求：
# 1. 使用unittest框架
# 2. 使用Fixture(setup、tearDown)
# 3. 浏览器最大化、隐式等待30秒
# 4. 使用断言判断登录用户是否为admin，不是则截屏保存图片
# 5. 图片命名格式为脚本执行时间(年月日时分秒)

# 导包
import time
import unittest
from selenium import webdriver
class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get("http://tpshop-test.itheima.net/")
    def tearDown(self):
        self.driver.quit()
    def test_login(self):
        self.driver.find_element_by_css_selector("#username").send_keys("18812345678")
        self.driver.find_element_by_css_selector("#password").send_keys("a123456")
        self.driver.find_element_by_css_selector("#verify_code").send_keys("8888")
        self.driver.find_element_by_css_selector(".J-login-submit").click()
        time.sleep(3)
        msg = self.driver.find_element_by_css_selector(".red ").text
        self.assertIn("admin",msg)
        if msg != "admin":
            file_path = "./test{}.png".format(time.strftime("%Y%m%d%H%M%S"))
            self.driver.get_screenshot_as_file(file_path)



