# !/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：ApiAutoTest
@File ：conftest.py.py
@Author ：琴师
@Date ：2022/5/7 11:23 下午
'''
import pytest
import os
from utils.RequestsUtil import RequestLogic
from utils.YamlUtil import YamlReader
from config import Conf
from config.Conf import ConfigYaml



@pytest.fixture(scope="session")
def get_loginToken():
    url = ConfigYaml().get_conf_UmsTestUrl() + "/connect/oauth/tokens"
    data = {
        "grant_type": "password",
        "client_id": "gaodingx",
        "client_secret": "7da458070e57b98e11d00d9286f23537",
        "os": "mac os",
        "mobile_area_code": 86,
        "mobile": "18218080002",
        "password": "111111"}
    response_json = RequestLogic().request_post(url=url, data=data)
    return response_json.get("body").get("access_token")




