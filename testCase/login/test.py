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
from unittestreport import rerun
class tc_login(unittest.TestCase):
    def setUp(self):
            pass

    def test_loginSuccess(self):
        """测试登录成功"""
        # self.driver = webdriver.Ie()
        # self.driver.implicitly_wait(30)  # 隐性等待时间为30秒
        # self.driver.get("https://www.baidu.com/")
        # self.driver.close()
        if self.assertEqual(1,1,"xxx"):
            print("123")

    @rerun(count=3, interval=2)
    def test_loginNull(self):
        """测试登录空测试"""
        self.assertEqual(1, 2, "xxx")
        print("开始测试登录空测试")

    def test_loginNameError(self):
        """测试登录名错误"""
        print("开始测试删除成员信息")


    def test_loginPWDError(self):
        """测试登录密码错误"""
        print("开始测试登录密码错误")


    def tearDown(self):
        print("测试结束")


if __name__ == "__main__":
    unittest.main()