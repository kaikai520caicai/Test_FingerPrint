"""
1. 对象库层-基类，把定位元素的方法定义在基类中
"""
from selenium.webdriver.support.wait import WebDriverWait

from utils import DriverUtils

"""
1.定义一个对象库层的基类
2.实现元素定位公用方法
3.修改要调用元素定位地方(对象层)
"""


class BasePage:

    # 定义初始化方法
    def __init__(self):
        # 获取浏览器驱动对象并赋值类的实例属性self.driver
        self.driver = DriverUtils.get_driver()

    # 实现元素定位公用方法
    def find_elt(self, location):  # find_elt(self,(By.ID, "username"))
        # 1.拷贝需要封装的代码的其中一份代码
        # 2.基于错误信息来进行修改
        return self.driver.find_element(*location)


# 2. 操作层-基类，把对元素执行输入操作的方法定义在基类中
"""
1.定义操作层的基类
2.定义公用的模拟输入方法
3.修改调用的地方，通过继承的思想来调用父类的方法，实现模拟输入
"""


class BaseHandle:
    # 不能去创建子类的对象
    # 不能去继承的对象

    # 公用的模拟输入的方法
    def input_text(self, element, text):
        # 1.拷贝需要封装的代码的其中一份代码
        # 2.基于错误信息来进行修改
        element.clear()
        element.send_keys(text)


# 1.定义函数
def to_swtich():
    # 2.拷贝其中的一份实现
    handles = DriverUtils.get_driver().window_handles
    DriverUtils.get_driver().switch_to.window(handles[-1])
    # 3.修改报错的地方


# 2.显示等待
def wait(element):
    return WebDriverWait(DriverUtils.get_driver(), 10, 0.5).until(lambda x: x.find_element(*element))
