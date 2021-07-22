import os
import logging.handlers

# 获取工程根目录
BASE_PATH = os.path.abspath(os.path.dirname(__file__))


# 日志配置方法
def basic_log_config():
    # 1.创建日志器
    logger = logging.getLogger()
    # 2.设置日志级别
    logger.setLevel(level=logging.INFO)
    # 3.创建每日生成一个日志文件的处理器
    lht = logging.handlers.TimedRotatingFileHandler(filename=BASE_PATH + "/log/webAutoTest.log", when="midnight",
                                                    interval=1,
                                                    backupCount=3)
    # 4.创建输出到控制台的处理
    ls = logging.StreamHandler()
    # 5.创建格式化器
    lf = logging.Formatter(
        fmt="%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s")
    # 6.将格式化器绑定到处理器
    lht.setFormatter(lf)
    ls.setFormatter(lf)
    # 7.将处理器绑定到日志器
    logger.addHandler(ls)
    logger.addHandler(lht)
