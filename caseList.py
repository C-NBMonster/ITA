# encoding: utf-8
'''
@author: mirrorChen
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: 1667809009@qq.com
@software: mirrorCity
@file: caseList.py
@time: 2020/10/20 8:34
@desc:
'''
from testCase.login.testLogin import *
from testCase.member.testMemberInfo import *
from testCase.member.testMemberLevelInfo import *
from testCase.order.testOrderProcess import *
from testCase.order.testOrderList import *
from testCase.product.testProductInfo import *
from testCase.product.testProductCategory import *
from testCase.supplier.testSupplierInfo import *
from testCase.user.users import *

from common.commons import *
import unittest


class C_caseList(unittest.TestCase):

    def caseSet(self):
        caseSet=[
            c_login("test_loginSuccess"),
            c_login("test_loginNull"),
            c_login("test_loginNameError"),
            c_login("test_loginPWDError"),
            memberInfo("test_memberInfo"),
            memberInfo("test_memberInfoUpdate"),
            memberInfo("test_DeletememberInfo"),
            memberInfo("test_AddmemberInfo"),
            MemberLevelInfo("test_getMemberLevelInfo"),
            MemberLevelInfo("test_changeMemberLevelInfo"),
            orderList("test_getOrderList"),
            orderList("test_OrderListUpdate"),
            orderList("test_OrderStatus"),
            orderProcess("test_orderStatusChange"),
            orderProcess("test_OrderFullProcess"),
            productCategory("test_getProductCategory"),
            productCategory("test_productCategoryUpdate"),
            productInfo("test_getProductInfo"),
            productInfo("test_getSubProductInfo"),
            supplierInfo("test_getSupplierInfo"),
            supplierInfo("test_DeleteSupplierInfo"),
            register("test_registerNull"),
            register("test_registerSuccess"),
            register("test_registerUserNameError"),
            register("test_registerPWDError"),
            updatePWD("test_updatePWD"),
            updatePWD("test_updatePWDFailed")
            ]
        return caseSet


    def get_xls_case(self):
        casePath = os.path.join(readConfig.proDir, "testFile", "interfaces.xlsx")
        xlsContent = get_xls_BySheetName(casePath, "allCases")
        return xlsContent


if __name__ == "__main__":

    tlc = []
    tc = C_caseList()
    C_caseList = tc.caseSet() #获取需要执行的type类型为class对象的case集合
    # X_caseList = [] #用于存储筛选完的需要执行的用例
    # F_caseList = []
    # xcontent = tc.get_xls_case()
    # suite = unittest.TestSuite()
    # for x in range(1,len(xcontent)):
    #      if str(xcontent[x][2]) !="" and not str(xcontent[x][2]).startswith("#"):
    #          X_caseList.append(xcontent[x][2])
    # for tc in X_caseList:
    #     lName = str(tc).split(".")
    #     F_caseList.append(lName[2])
    # for c in C_caseList:
    #     tn = str(c).split("(")
    #     for s in F_caseList:
    #         if str(tn[0]).strip() == str(s):
    #             suite.addTest(c)
    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(suite)
