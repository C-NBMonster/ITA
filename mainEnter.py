# encoding: utf-8
'''
@author: mirrorChen
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: 1667809009@qq.com
@software: mirrorCity
@file: mainEnter.py
@time: 2020/10/16 13:47
@desc:
'''

import os
import readConfig
import unittest
import HTMLTestRunner
from common.Log import Log,MyLog
from common import commons
from common import configEmail
from unittestreport import TestRunner
from caseList import C_caseList

def set_case_suite():

    #用例的控制应当做好，并且要做全，这样可以很好地控制用例的执行。
    #第一档，从模块级别进行控制loadTestsFromTestModule(module, pattern=None).此处的module是指装有测试用例的py文件
    #第二档，从测试类进行控制loadTestsFromTestCase(testCaseClass)，testCaseClass，即测试类，及其子类，孙类。类方法也可以用suite=unittest.TestSuite(unittest.makeSuite(TestDiv))添加
    #第三档，从测试类进行控制loadTestsFromName(name, module=None)，name是一个string，string需要是是这种格式的“module.class”.
    #加载单条用例tests=['test_001','test_002'] unittest.TestSuite(map(TestDiv,tests))map辅助，直接映射存储到测试套里面
    #第四档，加载大量（所有）用例，不加限制discover(start_dir, pattern=’test*.py’, top_level_dir=None)，从start_dir中获取文件自动加载所有匹配的用例

    #查看是否要运行所有用例
    runAll = readConfig.ReadConfig().get_runAll("runAllCases")
    test_suite = unittest.TestSuite()
    suite_model = []
    #如果运行所有，直接调用discover方法
    if runAll == "Yes":
        case_file = os.path.join(readConfig.proDir, "testCase")
        discover = unittest.defaultTestLoader.discover(case_file, pattern="test*" + '.py', top_level_dir=None)
        suite_model.append(discover)
        if len(suite_model) > 0:
            for suite in discover:
                for test_name in suite:
                    test_suite.addTest(test_name)
        else:
            return None
    else:
        casePath = os.path.join(readConfig.proDir, "testFile", "interfaces.xlsx")
        xlsContent = commons.get_xls_BySheetName(casePath, "allCases")
        caseSet = []
        testclass = []
        testclass2 = []
        caseList = []

        # 从模块级别加载需要运行的用例
        for i in range(1, len(xlsContent)):
            caseSet.append(xlsContent[i][2])
            if xlsContent[i][0] !="" and not str(xlsContent[i][0]).startswith("#"):
                testclass.append(xlsContent[i][1])

        # 从类级别加载需要执行的用例
        for j in range(0, len(testclass)):
            if not str(testclass[j]).startswith("#"):
                #剔除不需要运行的测试类
                testclass2.append(testclass[j])

        #去重，得出最后的测试类.不改变原来顺序
        caseClass = list(set(testclass2))
        caseClass.sort(key=testclass2.index)

        #从单条用例级别加载所需执行的用例
        for cs in caseSet:
            tp = str(cs).split(".")
            # 关联需要测试的类
            for sn in caseClass:
                if str(tp[1]).strip() == str(sn).strip() and not str(tp[0]).startswith("#"):
                    print(tp[2])
                    caseList.append(tp[2])

        #根据得出的最终测试用例，加载进入测试套
        c_caseSet = C_caseList().caseSet()
        for tc in c_caseSet:
            tn = str(tc).split("(")
            cName = str(tn[0]).strip()
            if not cName.startswith("#") and cName in caseList:
                test_suite.addTest(tc)
    return test_suite


def run():
    logger = MyLog("开启日志线程记录").get_log()
    logpath = Log("获取日志路径").logPath
    reportName = logpath + "\/"+'report.html'
    try:
        suit = set_case_suite()
        if suit is not None:
            logger.info("********TEST START********")
            with open(reportName, "w", encoding="UTF-8") as fp:
                fp.close()
            # with open(reportName,"wb") as fp:
                # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Test Report', verbosity=2, description='Test Description')
                # runner.run(suit)
                #rnn = TestRunner()
            rnn = TestRunner(suite=suit,filename="report.html",report_dir=logpath,title="testreport",tester="cjx",desc="test schemer report")
            rnn.run()
            #全部重跑,所有失败的用例都将重跑2次
            #rnn.rerun_run(count=3, interval=2)
        else:
            logger.info("Have no case to test.")
    except Exception as ex:
        logger.error(str(ex))
    finally:
        logger.info("*********TEST END*********")
        # send test report by email
        on_off = readConfig.ReadConfig().get_email("on_off")
        if int(on_off) == 0:
            configEmail.Email().send_email()
        elif int(on_off) == 1:
            logger.info("不发送邮件给开发")
        elif int(on_off) == 2:
            logger.info("不发送邮")
        else:
            logger.info("Unknow state.")



#print(set_case_suite())
run()
