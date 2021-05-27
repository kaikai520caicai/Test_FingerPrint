# _*_ coding: utf-8 _*_
# @Time    :2021/5/21 13:59
# @Author  :George
# @File    :test_baidu.py
# @Software:PyCharm
import unittest,time
from selenium import webdriver


class Test_baidu(unittest.TestCase):
    def setUp(self) :
        # 创建浏览器驱动对象
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10) #隐式等待10秒
        self.base_url = "https://www.baidu.com/"

    def tearDown(self) :
        self.driver.quit()
    @unittest.skip("不想执行")
    def test_login(self):
       driver =  self.driver
       driver.get(self.base_url)
       driver.find_element_by_id("kw").click()
       driver.find_element_by_id("kw").send_keys("python")
       driver.find_element_by_id("su").click()
       time.sleep(3)
       title = driver.title
       self.assertEqual(title,"python_百度搜索")

if __name__ =="__main__":
    unittest.main()

