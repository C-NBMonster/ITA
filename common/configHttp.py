# encoding: utf-8
'''
@author: mirrorChen
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: 1667809009@qq.com
@software: mirrorCity
@file: configHttp.py
@time: 2020/10/16 21:47
@desc:
'''
import requests
import readConfig
import urllib3
import urllib
import json
from common.Log import Log

localReadConfig = readConfig.ReadConfig()

class ConfigHttp:
    def __init__(self):
        global host, port, timeout
        host = localReadConfig.get_http("baseurl")
        port = localReadConfig.get_http("port")
        timeout = localReadConfig.get_http("timeout")
        self.log = Log("HttpRequestLog")
        self.logger = self.log.logger
        self.headers = {}
        self.params = {}
        self.data = {}
        self.url = None
        self.files = {}

    def set_url(self, url):
        self.url = host + url

    def set_headers(self, header):
        self.headers = header

    def set_params(self, param):
        self.params = param

    def set_data(self, data):
        self.data = data

    def set_files(self, file):
        self.files = file

    # defined http get method
    def get(self):
        try:
            response = requests.get(self.url, params=self.params, headers=self.headers, timeout=float(timeout))
            # response.raise_for_status()
            return response
        except TimeoutError:
            self.logger.error("Time out!")
            return None

    # defined http post method
    def post(self):
        try:
            response = requests.post(self.url, headers=self.headers, data=self.data, files=self.files, timeout=float(timeout))
            # response.raise_for_status()
            return response
        except TimeoutError:
            self.logger.error("Time out!")
            return None

    def apicall(self,method,url,getparams,postparams, headers=None):

        str1=''
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'

        tokens = 'Authorization: Bearer ' + str(self.tk)
        #添加头信息
        headers = {'User-Agent': user_agent,
                 'Content-Type': 'application/json',
                 'token': tokens
                 }
        result = ''
        #urllib3方法实现get,但没试验过
        # if method=='GET':
        #     if getparams!="":
        #         hp = urllib3.PoolManager()
        #         resp = hp.request("GET","http://www.baidu.com",body=data)
        #         result = resp.data.decode()
        #         return result


        #GET方法调用
        if method=='GET':
            if getparams!="":
                for k in getparams:
                    str1=str1+k+'='+urllib.request.quote(str(getparams.get(k)))
                    if len(getparams) > 2:
                        str1=str1+"&"
                url=url+"&"+str1
            result = urllib.request.urlopen(url).read()
        #POST方法调用
        response = ''
        if method=='POST':
            if postparams != "":
                http = urllib3.PoolManager()
                data = json.dumps(postparams, skipkeys=True)#urllib.parse.urlencode(postparams).encode(encoding="UTF-8")
                #req = urllib.request.Request(url, data, headers)
                response = http.request("POST",url, body=data, headers=headers) #urllib.request.urlopen(req)
        jsdata=json.loads(response.data)
        return jsdata
