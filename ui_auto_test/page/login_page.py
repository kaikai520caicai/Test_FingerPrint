"""
登陆页面的PO文件
"""
from selenium.webdriver.common.by import By
from base.base_page import BasePage, BaseHandle

# 1.今天第一轮PO，模模糊糊很正常，对着代码能敲出来，有一个简单的理解即可
# 2.学习较好的同学，可以去实现下其它的场景，例如后台管理系统发布商品等等


"""
容易犯错的问题：
1.在封装对象库层实例方法的时候容易遗漏return
2.在操作层和业务层进行实例化对象的时候容易遗漏括号
3.注意对齐方式
4.在编写初始化方法时不要把__init__错误写成,def __int__(self):  def __index__(self):
5.在调用方法时，方法整个变黄，检查定义该方法的位置和你调用的名称是否一致，在调用方法时尽量使用智能提示进行选择
"""

"""
对象库层：
1.定义对象库层类，继承对象库层基类，记住导包
2.定义对象库层初始化方法，重写父类初始化方法
3.定义对象库层实例属性，当前py文件所代表的页面所有要操作的元素，都定义一个实例属性来表示
4.实例属性赋值，通过实例属性来管理定位信息，值的类型为元组(含2个元素)，一个元素为By类提供的定位方法，第二个元素为选中定位方式后所对应的值
5.定义对象库层实例方法，当前py文件所代表的页面所要用的元素，都定义一个对应的找元素实例方法
6.实现实例方法，通过继承方式调用基类中公用的元素定位方法，找到元素对象，并且返回
"""


# 对象库层:专门封装界面上所有要操作的元素，并且找到这些元素进行统一管理
class LoginPage(BasePage):
    # 要使用父类的方法：
    # 1.在类名后面打上括号，括号中放置要继承的父类，然后导包
    # 2.如果子类有初始化方法且父类也有初始化方法，则需要重写父类的初始化方法
    # 3.调用父类公用的元素定位方法来调整子类代码

    def __init__(self):
        # 重写父类的初始化方法
        super().__init__()
        # 浏览器驱动的实例属性
        # self.driver = DriverUtils.get_driver()
        # 用户名输入框
        self.username = (By.ID, "username")  # 要定位用户输入框定位方式用的是ID，id属性值为username
        # 密码输入框
        self.password = (By.ID, "password")
        # 验证码输入框
        self.code = (By.ID, "verify_code")
        # 登陆按钮
        self.submit_btn = (By.NAME, "sbtbutton")
        # # 忘记密码
        # self.forget_password_link = (By.CSS_SELECTOR,".foget_pwt a")

    """
    将元素定位方式以及定位方式所对应的值抽离到实例属性中进行管理
    1.修改元素定位方法-元素定位的另外一种写法 find_element
    2.将定位方式和对应要求参数抽取到实例属性中
    3.优化参数的传递
    """

    # 找到用户名输入框
    def find_username(self):
        # 浏览器驱动对象.元素定位方法找到元素
        # return self.driver.find_element_by_id("username")
        # return self.driver.find_element(By.ID, "username")
        # return self.driver.find_element(self.username[0], self.username[1])
        # return self.driver.find_element(*self.username)
        # 通过调用父类中元素定位方法来定位元素
        return self.find_elt(self.username)

    # 找到密码输入框
    def find_password(self):
        return self.find_elt(self.password)

    # 找到验证码输入框
    def find_code(self):
        return self.find_elt(self.code)

    # 找到登陆按钮
    def find_submit_btn(self):
        return self.find_elt(self.submit_btn)


"""
操作层：
1.定义操作层类，继承操作层基类，记住导包
2.定义操作层初始化方法，在初始化方法中创建对象库层对象，并定义一个实例属性来承接
3.定义操作层操作方法，当前py文件所代表的页面所有要操作的元素都定义一个操作方法，如输入、点击等，部分特殊的另外处理
4.实现操作层操作方法，通过第2步实例属性来调用对象库层的实例方法找到元素对象后执行常用元素操作方法
"""


# 操作层:封装所有元素对象的操作方法
class LoginHandle(BaseHandle):
    # 1.在类名后加上括号，输入要继承的类，然后记得导包
    # 2.修改需要调用父类方法的代码

    def __init__(self):
        # 实例化对象库层
        self.login_page = LoginPage()

    # 用户名输入
    def input_username(self, username):
        # 找到用户名的元素对象
        self.input_text(self.login_page.find_username(), username)

    # 密码输入
    def input_password(self, pwd):
        # 调用父类方法来模拟输入密码
        self.input_text(self.login_page.find_password(), pwd)

    # 验证码输入
    def input_code(self, code):
        # self.login_page.find_code().clear()
        # self.login_page.find_code().send_keys(code)
        # 调用父类方法来模拟验证码输入
        self.input_text(self.login_page.find_code(), code)

    # 登陆的点击
    def click_submit_btn(self):
        self.login_page.find_submit_btn().click()


class LoginProxy:

    def __init__(self):
        # 定义一个实例属性用例存储操作层的对象
        self.login_handle = LoginHandle()

    # 定义业务方法:登陆
    def test_login(self, username, pwd, code):
        # 1.输入用户名
        self.login_handle.input_username(username)
        # 2.输入密码
        self.login_handle.input_password(pwd)
        # 3.输入验证码
        self.login_handle.input_code(code)
        # 4.点击登陆按钮
        self.login_handle.click_submit_btn()
