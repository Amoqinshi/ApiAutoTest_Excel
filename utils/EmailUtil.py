# !/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：ApiAutoTest 
@File ：EmailUtil.py
@Author ：琴师
@Date ：2022/5/13 10:57 上午 
'''
from email.mime.multipart import  MIMEMultipart
from email.mime.text import MIMEText
from config.Conf import ConfigYaml
import smtplib

smtp_server = ConfigYaml().get_email_info().get("smtpserver")
username = ConfigYaml().get_email_info().get("username")
password = ConfigYaml().get_email_info().get("password")
receiver = ConfigYaml().get_email_info().get("receiver")

class EmailSend(object):

    def __init__(self,smtp_server,username,pwd,receiver,title,content=None,file=None):
        self.smtp_server = smtp_server
        self.username = username
        self.pwd = pwd
        self.receiver = receiver
        self.title = title
        self.content = content
        self.file = file


    def send_email(self):
        msg = MIMEMultipart()
        msg.attach(MIMEText(self.content,_charset="utf-8"))
        msg["Subject"] = self.title
        msg["From"] = self.username
        msg["To"] = self.receiver
        if self.file:
            att = MIMEText(open(self.file).read())
            att["Content-Type"] = "application/octet-stream"
            att["Content-Dispostion"] = "attachment;filename = {}".format(self.file)
            msg.attach(att)
        # 登陆邮件服务器
        self.smtp = smtplib.SMTP(self.smtp_server,port=25)
        self.smtp.login(self.username,self.pwd)
        # 发送邮件
        self.smtp.sendmail(self.username,self.receiver,msg.as_string())


if __name__=="__main__":
    pass



