# encoding: utf-8
'''
@author: mirrorChen
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: 1667809009@qq.com
@software: mirrorCity
@file: testSupplierInfo.py
@time: 2020/10/17 22:04
@desc:
'''
import unittest
from selenium import webdriver
from common.Log import MyLog
class supplierInfo(unittest.TestCase):
    def setUp(self):
        #self.log = Log.Log("supplierInfo")
        self.log = MyLog("supplierInfo").get_log()
        #self.driver = webdriver.Firefox()
        self.log.info("开始测试获取供应商信息")
        #self.driver.implicitly_wait(30)  # 隐性等待时间为30秒
        #elf.base_url = "https://www.baidu.com"


    def test_getSupplierInfo(self):
        """获取供应商信息"""
        self.log.info("开始测试获取供应商信息")
        self.log.info("测试成功")

    def test_DeleteSupplierInfo(self):
        """删除供应商信息"""
        self.log.info("开始测试删除供应商信息")
        self.log.info("测试成功")