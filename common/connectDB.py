# encoding: utf-8
'''
@author: mirrorChen
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: 1667809009@qq.com
@software: mirrorCity
@file: connectDB.py
@time: 2020/10/17 11:07
@desc:
'''
import pymysql
import readConfig
from common.Log import MyLog as Log

localReadConfig = readConfig.ReadConfig()

class MyDB:

    def __init__(self):
        self.log = Log.get_log()
        self.logger = self.log.get_logger()
        self.db = None
        self.cursor = None
        host = localReadConfig.get_db("host")
        username = localReadConfig.get_db("username")
        password = localReadConfig.get_db("password")
        port = localReadConfig.get_db("port")
        database = localReadConfig.get_db("database")
        self.config = {
        'host': str(host),
        'user': username,
        'passwd': password,
        'port': int(port),
        'db': database
        }

    def connectDB(self):
        try:
            # connect to DB
            self.db = pymysql.connect(self.config)
            # create cursor
            self.cursor = self.db.cursor()
            print("Connect DB successfully!")
            self.logger("Connect DB successfully!")
        except ConnectionError as ex:
            self.logger.error(str(ex))

    def executeSQL(self, sql, params):
        self.connectDB()
        # executing sql
        self.cursor.execute(sql, params)
        # executing by committing to DB
        self.db.commit()
        return self.cursor

    def get_all(self, cursor):
        value = cursor.fetchall()
        return value

    def get_one(self, cursor):
        value = cursor.fetchone()
        return value

    def closeDB(self):
        self.db.close()
        print("Database closed!")