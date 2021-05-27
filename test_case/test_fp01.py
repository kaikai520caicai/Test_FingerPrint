# _*_ coding: utf-8 _*_
# @Time    :2021/5/26 16:36
# @Author  :George
# @File    :test_fp01.py
# @Software:PyCharm
import unittest,time
from selenium import webdriver


class TestFp(unittest.TestCase):

    @classmethod
    def setUpClass(cls) :
        cls.driver = webdriver.Chrome()
        # driver = cls.driver
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.base_url = "http://docweb.arcsoft.com.cn/qa_statistic/index"
    @classmethod
    def tearDownClass(cls) :
        cls.driver.quit()

    def setUp(self) :
        self.driver.get(self.base_url)
    def tearDown(self) :
        print("完成条测试用例")
    # @unittest.skip("tiaoguo")
    def test_verison_management1(self):

        self.driver.find_element_by_xpath('//*[@id="components-layout-demo-fixed-sider"]/section/main/div/div[1]/div[2]/div/li[1]').click()
        self.driver.find_element_by_class_name("ant-select-selection__placeholder").click()
        self.driver.find_element_by_class_name('ant-select-dropdown-menu-item').click()
        self.driver.find_element_by_xpath('//*[@id="components-layout-demo-fixed-sider"]/section/main/div/div[1]/form/div[2]/div[2]/div/span/span/input').send_keys("v122")
        self.driver.find_element_by_xpath('//*[@id="components-layout-demo-fixed-sider"]/section/main/div/div[1]/form/div[3]/div[2]/div/span/span/input').send_keys("George")
        self.driver.find_element_by_class_name("ant-btn-primary").click()
        time.sleep(1)
        title = self.driver.find_element_by_class_name("ant-empty-description").text
        self.assertEqual(title,"暂无数据")
    def test_verison_management2(self):

        self.driver.find_element_by_xpath('//*[@id="components-layout-demo-fixed-sider"]/section/main/div/div[1]/div[2]/div/li[1]').click()
        self.driver.find_element_by_xpath('//*[@id="components-layout-demo-fixed-sider"]/section/main/div/div[1]/div/div/div/div/div/div/table/tbody/tr[4]/td[15]/span/a[1]').click()
        self.driver.find_element_by_css_selector('[placeholder="HAL版本"]').send_keys("2.20012452")
        time.sleep(1)
        element = self.driver.find_element_by_xpath("//*[contains(text(),'完')]")
        self.driver.execute_script("arguments[0].click();",element)
        title = self.driver.find_element_by_xpath('//*[contains(text(),"提")]').text
        self.assertIn(title,"提交成功!")
    def test_verison_management3(self):
        self.driver.find_element_by_xpath("//div/*[contains(text(),'版本')]").click()
        self.driver.find_element_by_css_selector('[placeholder="请输入TEE版本"]').send_keys("181")
        self.driver.find_element_by_css_selector('[placeholder="请输入创建者"]').send_keys("郑自")
        self.driver.find_element_by_class_name("ant-btn-primary").click()
        time.sleep(1)
        text = self.driver.find_element_by_css_selector('[title = "郑自财"]').text
        self.assertEqual(text,"郑自财")
    def test_verison_management4(self):
        self.driver.find_element_by_xpath("//div/*[contains(text(),'版本')]").click()
        self.driver.find_element_by_css_selector('[placeholder="请输入TEE版本"]').send_keys("1111")
        self.driver.find_element_by_css_selector('[placeholder="请输入创建者"]').send_keys("郑自")
        self.driver.find_element_by_class_name("ant-btn-primary").click()
        time.sleep(1)
        title = self.driver.find_element_by_class_name("ant-empty-description").text
        self.assertEqual(title,"暂无数据")
    def test_verison_management4(self):
        self.driver.find_element_by_xpath("//div/*[contains(text(),'版本')]").click()
        self.driver.find_element_by_css_selector('[placeholder="请输入TEE版本"]').send_keys("181")
        # self.driver.find_element_by_css_selector('[placeholder="请输入创建者"]').send_keys("郑自")
        self.driver.find_element_by_class_name("ant-btn-primary").click()
        time.sleep(1)
        text = self.driver.find_element_by_css_selector('[title = "郑自财"]').text
        self.assertEqual(text,"郑自财")



    # @unittest.skip("skip")
    def test_case_management(self):
        pass
    def test_case_management1(self):
        pass
    def test_case_management2(self):
        pass
    def test_case_management3(self):
        pass
    def test_case_management4(self):
        pass
    def test_case_management5(self):
        pass
    def test_case_management6(self):
        pass





if __name__== "__main__":
    unittest.main()


