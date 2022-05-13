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
from utils.LogUtil import my_log
from utils.EmailUtil import EmailSend
import json,re,subprocess



p = r"\${(.+)}\$"
smtp_server = ConfigYaml().get_email_info().get("smtpserver")
username = ConfigYaml().get_email_info().get("username")
password = ConfigYaml().get_email_info().get("password")
receiver = ConfigYaml().get_email_info().get("receiver")


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

def allure_report(report_path,report_html):
    """
    生成allure测试报告
    :param report_path:
    :param report_html:
    :return:
    """
    cmd = "allure generate {} -o {} --clean".format(report_path,report_html)
    # my_log().log("生成测试报告")
    try:
        subprocess.call(cmd,shell=True)
    except Exception as e:
        my_log().error("执行报告生成失败，请检查一下测试环境相关配置")

def send_email(report_html_path="",title="测试",content="内容"):
    """
    发送邮件
    :param report_html_path:
    :param title:
    :param content:
    :return:
    """

    A = EmailSend(smtp_server=smtp_server,
                  username=username,
                  pwd=password,
                  receiver=receiver,
                  title=title,
                  content=content,
                  file=report_html_path)
    A.send_email()



if __name__=="__main__":
    # print(res_sub('{"authorization":"Bearer ${token}$", "x-business-id": "1", "x-channel-id": "8"}',"123"))
    # print(data_find('{"authorization":"Bearer ${token}$", "x-business-id": "1", "x-channel-id": "8"}'))
    # print(res_find('{"authorization":"Bearer ${token}$", "x-business-id": "1", "x-channel-id": "8"}'))
    # pattern = '{"authorization":"Bearer ${token}$", "x-business-id": "1", "x-channel-id": "8"}'
    # print(res_find(pattern))
    pass