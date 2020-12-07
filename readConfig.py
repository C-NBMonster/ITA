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
import codecs
import configparser


#proDir = os.path.split(os.path.realpath(__file__))[0] #当前文件所在的上级目录,该函数返回路径名，和文件名
proDir = os.path.dirname(os.path.realpath(__file__)) #当前文件所在的上级目录,该函数返回路径名，和文件名
cfgPath=os.path.join(proDir,"config.ini")
# print("proDir:",proDir)
# print("cfgPath:",cfgPath)

class ReadConfig:
    def __init__(self):
        fd = open(cfgPath)
        data = fd.read()

        #  remove BOM
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            file = codecs.open(cfgPath, "w")
            file.write(data)
            file.close()
        fd.close()

        self.cf = configparser.ConfigParser()
        self.cf.read(cfgPath)

    def get_email(self, name):
        value = self.cf.get("EMAIL", name)
        return value

    def get_http(self, name):
        value = self.cf.get("HTTP", name)
        return value

    def get_db(self, name):
        value = self.cf.get("DATABASE", name)
        return value

    def get_runAll(self, name):
        value = self.cf.get("RUNALL", name)
        return value

if __name__=="__main__":
    testC= ReadConfig()
    print(testC.get_email("mail_host"))
