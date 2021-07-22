# 1.导包
import time
import unittest
from BeautifulReport import BeautifulReport

# 2.组织测试套件
from config import BASE_PATH
from utils import DriverUtils

suite = unittest.TestLoader().discover(BASE_PATH + "/case", "test*.py")

# 3.定义测试报告文件名
report_file = "{}-report.html".format(time.strftime("%Y%m%d%H%M%S"))

# 将关闭浏览的开关关掉
DriverUtils.check_open_key(False)

# 4.使用BeautifulReport来批量运行测试用例并且生成测试报告
BeautifulReport(suite).report(filename=report_file, description="webAutoTest", log_path=BASE_PATH + "/report")

# 将关闭浏览器的开关又打开
DriverUtils.check_open_key(True)
DriverUtils.quit_driver()
