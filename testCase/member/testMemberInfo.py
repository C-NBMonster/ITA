# encoding: utf-8
'''
@author: mirrorChen
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: 1667809009@qq.com
@software: mirrorCity
@file: testMemberInfo.py
@time: 2020/10/17 22:03
@desc:
'''

import unittest
from selenium import webdriver
from common.Log import MyLog
class memberInfo(unittest.TestCase):
    def setUp(self):
        #self.log = Log.Log("memberInfo")
        self.log = MyLog("memberInfo").get_log()
        #self.driver = webdriver.Firefox()
        self.log.info("开始测试获取会员信息")
        #self.driver.implicitly_wait(30)  # 隐性等待时间为30秒
        #self.base_url = "https://www.baidu.com"


    def test_memberInfo(self):
        """测试获取成员信息"""
        self.log.info("开始测试获取会员信息")
        self.log.info("测试成功")

    def test_memberInfoUpdate(self):
        """测试更新成员信息"""
        self.log.info("开始测试更新会员信息")
        self.log.info("测试成功")

    def test_DeletememberInfo(self):
        """测试删除成员信息"""
        self.log.info("开始测试删除会员信息")
        self.log.info("测试成功")

    def test_AddmemberInfo(self):
        """测试添加成员信息"""
        self.log.info("开始测试添加会员信息")
        self.log.info("测试成功")



