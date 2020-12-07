# encoding: utf-8
'''
@author: mirrorChen
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: 1667809009@qq.com
@software: mirrorCity
@file: testMemberLevelInfo.py
@time: 2020/10/17 22:06
@desc:
'''
import unittest
import time
from common.Log import MyLog
class MemberLevelInfo(unittest.TestCase):
    def setUp(self):
        #self.log = Log.Log("MemberLevelInfo")
        self.log = MyLog("MemberLevelInfo").get_log()
        #self.driver = webdriver.Firefox()
        self.log.info("开始测试获取会员等级信息")
        #self.driver.implicitly_wait(30)  # 隐性等待时间为30秒
        #self.base_url = "https://www.baidu.com"


    def test_getMemberLevelInfo(self):
        time.sleep(3)
        self.log.info("开始测试获取会有等级信息")
        self.log.info("测试成功")

    def test_changeMemberLevelInfo(self):
        self.log.info("开始测试更改会有等级信息")
        self.log.info("测试成功")