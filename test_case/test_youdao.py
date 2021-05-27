# _*_ coding: utf-8 _*_
# @Time    :2021/5/21 13:59
# @Author  :George
# @File    :test_youdao.py
# @Software:PyCharm
import unittest,time
from selenium import webdriver

class Testyoudao(unittest.TestCase):
    def setUp(self) :
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.base_url = "http://www.youdao.com/"

    def tearDown(self) :
        self.driver.quit()
    @unittest.skip("skip")
    def test_youdao(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("translateContent").clear()
        driver.find_element_by_id("translateContent").send_keys("勇气")
        driver.find_element_by_id("translateContent").submit()
        time.sleep(3)
        title = driver.title
        self.assertEqual(title,"【勇气】英语怎么说_在线翻译_有道词典")


if __name__=="__main__":
    unittest.main()
