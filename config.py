# _*_ coding: utf-8 _*_
# @Time    :2021/5/28 9:56
# @Author  :George
# @File    :utils.py
# @Software:PyCharm

import logging
import os,time
# 获取工程根目录
BASE_PATH = os.path.abspath(os.path.dirname(__file__))
# 日志配置函数
def log_config():
    # 创建日志器
    logger = logging.getLogger()
    # 设置日志级别
    logger.setLevel(level=logging.INFO)
    # 创建每日生成一个日志文件的处理器
    lht = logging.handlers.TimedRotatingFileHandler(filename=BASE_PATH + "/log/{}FingerPrint.log".format(time.strftime("%Y%m%d%H%M%S")), when="midnight",
                                                    interval=1,
                                                    backupCount=3)
    # 创建输出到控制台的处理
    ls = logging.StreamHandler()
    # 创建格式化器
    lf = logging.Formatter(
        fmt="%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s")
    # 将格式化器绑定到处理器
    lht.setFormatter(lf)
    ls.setFormatter(lf)
    # 将处理器绑定到日志器
    logger.addHandler(ls)
    logger.addHandler(lht)


