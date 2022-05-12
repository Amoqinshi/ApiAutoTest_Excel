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
import json,re


p = r"\${(.+)}\$"

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


def json_parse(data):
    """
    格式化字符串转换json格式
    :param data:
    :return:
    """
    return json.loads(data) if data else data


def res_find(data,pattern=p):
    """
    查询
    :param data:
    :return:
    """
    p = re.compile(pattern)
    result = p.search(data).group(1)
    return  result


def res_sub(data,replace,pattern=p):
    """
    替换
    :param data:
    :param replace:
    :param pattern:
    :return:
    """
    p = re.compile(pattern)
    result = p.search(data).group(1)
    if result:
        return re.sub(pattern,replace,data)
    return result


def data_find(headers):
    """
    验证请求中是否有${}$的需要进行结果关联
    :param headers:
    :return:
    """
    if "${" in headers:
        headers = res_find(headers)
    return headers


if __name__=="__main__":
    print(res_sub('{"authorization":"Bearer ${token}$", "x-business-id": "1", "x-channel-id": "8"}',"123"))
    # print(data_find('{"authorization":"Bearer ${token}$", "x-business-id": "1", "x-channel-id": "8"}'))
    # print(res_find('{"authorization":"Bearer ${token}$", "x-business-id": "1", "x-channel-id": "8"}'))
    # pattern = '{"authorization":"Bearer ${token}$", "x-business-id": "1", "x-channel-id": "8"}'
    # print(res_find(pattern))
    # pass