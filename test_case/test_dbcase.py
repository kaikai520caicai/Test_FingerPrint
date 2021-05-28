# _*_ coding: utf-8 _*_
# @Time    :2021/5/27 20:43
# @Author  :George
# @File    :test_dbcase.py
# @Software:PyCharm
import time,unittest
from selenium import webdriver


class  Test_DbCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) :
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.base_url = "http://docweb.arcsoft.com.cn/qa_statistic/index"
    @classmethod
    def tearDownClass(cls) :
        cls.driver.quit()
    def setUp(self) :
        self.driver.get(self.base_url)
    def tearDown(self) :
        print("over testcase")


    def test_dbcase01(self):
        self.driver.find_element_by_xpath("//*[contains(text(),'测试集')]").click()
        self.driver.find_element_by_xpath("//*[contains(text(),'测试集标签')]").send_keys("25")
        self.driver.find_element_by_xpath('//*[contains(text(),"查")]').click()
        time.sleep(1)
        title = self.driver.find_element_by_xpath('//*[contains(text(),"条")]')
        self.assertEqual(title,"共 1 条")



