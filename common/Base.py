# !/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：ApiAutoTest 
@File ：Base.py
@Author ：琴师
@Date ：2022/5/5 3:57 下午 
'''

from config.Conf import ConfigYaml
from utils.MysqlUtil import ConnectDatabase



def init_db(DB_type):
    db_info = ConfigYaml().get_db_conf(DB_type)
    host = db_info.get("db_host")
    user = db_info.get("db_user")
    pwd = db_info.get("db_pwd")
    db_name = db_info.get("db_name")
    charset = db_info.get("db_charset")
    port = int(db_info.get("db_port"))
    database = ConnectDatabase(host,user,pwd,db_name,charset,port)
    print(database)
    return database


if __name__=="__main__":
    init_db("DB_Test")