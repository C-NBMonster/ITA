# encoding: utf-8
'''
@author: mirrorChen
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: 1667809009@qq.com
@software: mirrorCity
@file: t2.py
@time: 2020/11/25 20:05
@desc:
'''

import logging
import time
import os


class Logger:
    @classmethod
    def logger(cls):
        file_path = "../resource/log/%s/" % time.strftime("%Y%m%d")
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        file_name = file_path + '%s_log.log' % (time.strftime("%Y%m%d"))
        logging.basicConfig(
            level=logging.INFO,
            format='%(levelname)s %(asctime)s %(filename)s[line:%(lineno)d] %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
            filename=file_name,
            filemode='a'
        )
        return logging.getLogger()

    @classmethod
    def info(cls, text):
        Logger.logger().info(text)

    @classmethod
    def error(cls, text):
        Logger.logger().error(text)

    @classmethod
    def debug(cls, text):
        Logger.logger().debug(text)

    @classmethod
    def warning(cls, text):
        Logger.logger().warning(text)

    @classmethod
    def print_info(cls, text):
        print(text)
        Logger.logger().info(text)

    @classmethod
    def print_error(cls, text):
        print(text)
        Logger.logger().error(text)

    @classmethod
    def print_debug(cls, text):
        print(text)
        Logger.logger().debug(text)

    @classmethod
    def print_warning(cls, text):
        print(text)
        Logger.logger().warning(text)







