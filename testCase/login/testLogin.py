# encoding: utf-8
'''
@author: mirrorChen
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: 1667809009@qq.com
@software: mirrorCity
@file: testLogin.py
@time: 2020/10/17 22:01
@desc:
'''
import unittest
import time
from common.Log import MyLog

class c_login(unittest.TestCase):
    def setUp(self):
        #self.log = Log("login")
        self.log = MyLog("c_login").get_log()
        #self.log = Log.Log("memberInfo").logger
        self.log.info("开始测试登录")

    def test_loginSuccess(self):
        """测试登录成功"""
        time.sleep(2)
        # self.driver = webdriver.Ie()
        # self.driver.implicitly_wait(30)  # 隐性等待时间为30秒
        # self.driver.get("https://www.baidu.com/")
        # self.driver.close()
        self.log.info("开始测试登录成功")
        self.log.info("测试成功")


    def test_loginNull(self):
        """测试登录空测试"""
        self.log.info("开始测试登录空测试")
        self.log.info("测试成功")

    def test_loginNameError(self):
        """测试登录名错误"""
        self.log.info("开始测试登录名错误")
        self.log.info("测试成功")

    def test_loginPWDError(self):
        """测试登录密码错误"""
        self.log.info("开始测试登录密码错误")
        self.log.info("测试成功")

    def tearDown(self):
        self.log.info("测试结束")

