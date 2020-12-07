# encoding: utf-8
'''
@author: mirrorChen
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: 1667809009@qq.com
@software: mirrorCity
@file: Log.py
@time: 2020/10/16 21:18
@desc:
'''
import logging
from datetime import datetime
import threading
import os, time
import readConfig


class Log:
    def __init__(self, logModule):
        proDir = readConfig.proDir
        self.resultPath = os.path.join(proDir, "result")
        # create result file if it doesn't exist #项目根目录下添加result文件夹
        if not os.path.exists(self.resultPath):
            os.mkdir(self.resultPath)
        # defined test result file name by localtime，每次测试log,report文件放一个文件夹中
        self.logPath = os.path.join(self.resultPath, str(datetime.now().strftime("%Y%m%d%H%M%S")))
        # create test result file if it doesn't exist
        if not os.path.exists(self.logPath):
            os.mkdir(self.logPath)


        # defined logger
        self.logger = logging.getLogger(logModule)
        # defined log level
        self.logger.setLevel(logging.DEBUG)
        #利用logging.basicConfig()打印信息到控制台
        logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                            level=logging.DEBUG)


    def get_logger(self, level, message):
        # defined handler
        f_handler = logging.FileHandler(os.path.join(self.logPath, "output.log"), "a+", encoding='utf-8')
        # defined formatter
        #self.formatter = logging.Formatter('[%(asctime)s] - %(filename)s] - %(levelname)s: %(message)s')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # defined formatter
        f_handler.setFormatter(formatter)
        #set the log level
        f_handler.setLevel(logging.DEBUG)
        # add handler
        self.logger.addHandler(f_handler)


        # # 创建一个StreamHandler,用于输出到控制台

        # c_handler = logging.StreamHandler()
        # c_handler.setLevel(logging.DEBUG)
        # c_handler.setFormatter(formatter)
        # self.logger.addHandler(c_handler)

        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        # 这两行代码是为了避免日志输出重复问题
        # self.logger.removeHandler(c_handler)
        self.logger.removeHandler(f_handler)
        # 关闭打开的文件
        f_handler.close()

    def debug(self, message):
        self.get_logger('debug', message)

    def info(self, message):
        self.get_logger('info', message)

    def warning(self, message):
        self.get_logger('warning', message)

    def error(self, message):
        self.get_logger('error', message)



class MyLog:
    log = None
    mutex = threading.Lock()

    def __init__(self,mName):
        self.module_Name = mName

    ##@staticmethod
    def get_log(self):
        if MyLog.log is None:
            MyLog.mutex.acquire()
            MyLog.log = Log(self.module_Name)
            MyLog.mutex.release()

        return MyLog.log

# if __name__ == '__main__':
#     log=Log("test")
#     log.info("开始测试日志调试脚本")
#     log.info("请输入日志调试等级")
#     log.error("有错误啦！")
#     log.warning("测试结束")