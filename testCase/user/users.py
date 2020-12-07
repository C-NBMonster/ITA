# encoding: utf-8
'''
@author: mirrorChen
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: 1667809009@qq.com
@software: mirrorCity
@file: users.py
@time: 2020/10/17 22:02
@desc:
'''

import unittest
from selenium import webdriver
from common.Log import MyLog
class register(unittest.TestCase):
    def setUp(self):
        #self.log = Log.Log("register")
        self.log = MyLog("memberInfo").get_log()
        #self.driver = webdriver.Firefox()
        self.log.info("开始测试注册")
        #self.driver.implicitly_wait(30)  # 隐性等待时间为30秒
        #self.base_url = "https://www.baidu.com"


    def test_registerNull(self):
        """注册空测试"""
        self.log.info("开始测试注册空测试")
        self.log.info("测试成功")


    def test_registerSuccess(self):
        """测试注册成功"""
        self.log.info("开始测试注册成功")
        self.log.info("测试成功")

    def test_registerUserNameError(self):
        """测试注册用户名错误"""
        self.log.info("开始测试注册用户名错误")
        self.log.info("测试成功")

    def test_registerPWDError(self):
        """测试注册密码不符合规则"""
        self.log.info("开始测试注册密码不符合规则")
        self.log.info("测试成功")

class updatePWD(unittest.TestCase):
    def setUp(self):
        self.log = Log.Log("updatPWD")
        self.log.info("开始测试修改密码")


    def test_updatePWD(self):
        """测试更新密码"""
        self.log.info("开始测试更新密码")
        self.log.info("测试成功")

    def test_updatePWDFailed(self):
        """测试更新密码失败"""
        self.log.info("开始测试更新密码失败")
        self.log.info("测试成功")