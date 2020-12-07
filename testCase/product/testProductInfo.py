# encoding: utf-8
'''
@author: mirrorChen
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: 1667809009@qq.com
@software: mirrorCity
@file: testProductInfo.py
@time: 2020/10/17 22:04
@desc:
'''
import unittest
from selenium import webdriver
from common.Log import Log,MyLog
class productInfo(unittest.TestCase):
    def setUp(self):
        #self.log = Log("productInfo")
        self.log = MyLog("productCategory").get_log()
        #self.driver = webdriver.Firefox()
        self.log.info("开始测试获取商品信息")
        #self.driver.implicitly_wait(30)  # 隐性等待时间为30秒
        #self.base_url = "https://www.baidu.com"


    def test_getProductInfo(self):
        """测试获取商品信息"""
        self.log.info("开始测试获取商品信息")
        self.log.info("测试成功")

    def test_getSubProductInfo(self):
        """测试获取商品子商品"""
        self.log.info("开始测试获取商品子商品信息")
        self.log.info("测试成功")