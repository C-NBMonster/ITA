# encoding: utf-8
'''
@author: mirrorChen
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: 1667809009@qq.com
@software: mirrorCity
@file: configsoap.py
@time: 2020/10/21 11:08
@desc:
'''
from suds.client import Client
from suds.xsd import sxbasic


def SoaRequest(wsdl,fnname,data): #soap接口调用方法
    sxbasic.resultList=[] #初始化location列表
    soaService = Client(wsdl).service
    soaRep = getattr(soaService,fnname)(data)
    return soaRep