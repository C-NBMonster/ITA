# encoding: utf-8
'''
@author: mirrorChen
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: 1667809009@qq.com
@software: mirrorCity
@file: testOrderList.py
@time: 2020/10/17 22:03
@desc:
'''

import unittest
from selenium import webdriver
from common.Log import MyLog
class orderList(unittest.TestCase):
    def setUp(self):
        #self.log = Log.Log("OrderList")
        self.log = MyLog("orderList").get_log()
        #self.driver = webdriver.Firefox()
        self.log.info("开始测试获取订单列表信息")
        #self.driver.implicitly_wait(30)  # 隐性等待时间为30秒
        #self.base_url = "https://www.baidu.com"


    def test_getOrderList(self):
        """测试获取订单列表信息"""
        self.log.info("开始测试获取订单列表信息")
        self.log.info("测试成功")

    def test_OrderListUpdate(self):
        """测试更新订单列表信息"""
        self.log.info("开始测试更新订单列表信息")
        self.log.info("测试成功")

    def test_OrderStatus(self):
        """测试获取订单列表状态信息"""
        self.log.info("开始测试获取订单列表状态信息")
        self.log.info("测试成功")