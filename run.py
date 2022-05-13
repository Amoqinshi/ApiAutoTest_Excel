# !/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：ApiAutoTest 
@File ：run.py
@Author ：琴师
@Date ：2022/5/4 2:59 下午 
'''
import os
import pytest
from config import Conf

if __name__=="__main__":
    report_path = Conf.get_report_path() + os.sep + "result"
    report_html_path = Conf.get_report_path() + os.sep + "html"
    pytest.main(["-s","--alluredir",report_path])
