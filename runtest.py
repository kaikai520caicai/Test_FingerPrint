# _*_ coding: utf-8 _*_
# @Time    :2021/5/21 13:59
# @Author  :George
# @File    :runtest.py
# @Software:PyCharm
# from test_case import test_baidu
# from  test_case import test_youdao
import unittest
from BeautifulReport import BeautifulReport
import time

# suite = unittest.TestSuite()
# suite.addTest(test_baidu.Test_baidu("test_login"))
# suite.addTest(test_youdao.Testyoudao("test_youdao"))
if __name__ =="__main__":
#     # runer = unittest.TextTestRunner()
#     # runer.run(suite)
    suite = unittest.defaultTestLoader.discover("./test_case",pattern="test*.py",top_level_dir=None)
    BeautifulReport(suite).report(filename="./report/{}测试报告".format(time.strftime("%Y%m%d%H%M%S")),description="指纹平台测试",log_path=".")

