import time
import json
from selenium import webdriver


# 定义浏览器驱动工具类
class DriverUtils:  # 自定义类名
    # 代表浏览器驱动对象的私有变量
    __driver = None  # 自定义是有属性

    # 定义一个关闭浏览器开关的属性
    __open_key = True

    # 获取浏览器驱动
    # 为了方便调用设置类级别的方法
    # 在封装方法时，如调用地方需要方法执行的数据就需要返回
    @classmethod  # 固定写法，类级别装饰器
    def get_driver(cls):  # 自定义方法
        # 判断浏览器驱动对象是为空
        if cls.__driver is None:  # 判断自己定义的类属性是否为空
            # 实例化浏览器驱动
            cls.__driver = webdriver.Chrome()  # 给自定义的类属性赋值，值等于浏览器驱动对象
            # 最大窗口，隐式等待
            cls.__driver.maximize_window()  # cls.__driver（浏览器驱动对象） maximize_window 最大化固定写法
            # 隐式等待
            cls.__driver.implicitly_wait(10)  # cls.__driver（浏览器驱动对象） implicitly_wait 隐式等待
        # 返回驱动对象
        return cls.__driver  # 返回cls.__driver（浏览器驱动对象

    # 修改开关值的方法
    @classmethod
    def check_open_key(cls, key):
        cls.__open_key = key

    # 关闭浏览器驱动对象的方法
    @classmethod  # 固定写法，类级别装饰器
    def quit_driver(cls):
        # print("浏览器开关值----------》", cls.__open_key)
        if cls.__driver is not None and cls.__open_key is True:
            # 关闭浏览器驱动对象
            time.sleep(2)  # 固定写法，休眠2s
            cls.__driver.quit()  # cls.__driver（浏览器驱动对象)关闭
            # 浏览器驱动在调用quit()关闭浏览器驱动对象但是__driver并不等于空
            # print(cls.__driver)
            cls.__driver = None


# 获取弹出框信息函数
def get_msg():  # 自定义函数
    # 6.打印异常提示框信息
    time.sleep(4)  # 固定写法，休眠2s
    msg = DriverUtils.get_driver().find_element_by_css_selector(".layui-layer-content").text
    # DriverUtils.get_driver()调用自己写好的类和方法获取浏览器驱动对象  然后调用元素定位的方法获取文本，msg为自定义变量，存储的是获取回来的文本
    print(msg)  # 打印获取异常信息文本
    return msg  # 返回获取文本信息


# 定义读取json测试数据并且组织成parameterized.expand所要求的数据格式的函数
# 1.定义读取数据的函数
def build_testData(file_path):
    # 测试完整数据存储的空格列表
    test_dict = []
    # 2.读取json文件
    with open(file_path, encoding="utf-8")as f:
        # 读取json文件的完整数据并且自动化转化为python字典数据
        json_str = json.load(f)
        # 3.获取一层键值
        for i in json_str.values():
            # 4.获取键值的所有键值
            # print(list(i.values()))
            test_dict.append(list(i.values()))
        # 5.返回组织好的测试
        print(test_dict)
    return test_dict
