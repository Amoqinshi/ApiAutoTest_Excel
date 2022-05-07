# !/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：ApiAutoTest 
@File ：test_Login.py
@Author ：琴师
@Date ：2022/5/4 4:01 下午 
'''
import json

import requests,yaml,os
from utils.RequestsUtil import RequestLogic
from utils.YamlUtil import YamlReader
from utils.AssertUtil import Assert
from utils.LogUtil import my_log
from config.Conf import ConfigYaml
from config import Conf
from common.Base import init_db
import pytest


test_file = os.path.join(Conf.get_caselist_path(),"test_Login.yml")
cast_list = YamlReader(test_file).reader_all()
class Test(object):

    def setup_class(self):

        self.Log = my_log(log_name=os.path.basename(__file__))
        self.request = RequestLogic()

    @pytest.mark.parametrize("login",cast_list)
    def test_login(self,login):
        """
        Case--密码登录(phone正常,pwd正常)
        """
        url = ConfigYaml().get_conf_UmsTestUrl() + login.get("Url")
        data = login.get("data")
        print(type(data))
        self.Log.info("request data：%s" % (str(data)))
        headers = login.get("headers")
        response_json = self.request.request_post(url=url,data=data)
        self.Log.info("response data：%s" % (str(response_json)))


    def teardowm_class(self):
        pass


if __name__=="__main__":
    pytest.main(["test_Login.py"])
# def test_Loginsend():
#     """
#     Case--密码登录(phone正常,pwd正常)
#     """
#     request = RequestLogic()
#     conf = ConfigYaml()
#     url = conf.get_conf_UmsReleaseUrl() + "/connect/oauth/tokens"
#     headers = {"Content-Type":"application/json","x-biz-code":"1"}
#     data = {"grant_type":"password","client_id":"gaodingx","client_secret":"7da458070e57b98e11d00d9286f23537","os":"mac os","mobile_area_code":86,"mobile":"15927101278","password":"000000"}
#     r = request.request_post(url=url,json=data,headers=headers)
#     print(r.get("body"))
#     conn = init_db("DB_Test")
#     res = conn.Select_Sql("select id,username from tb_users where username='python'")
#
#     Assert().assert_code(r.get("body").get("code"),res.get("id"))


#
#
# if __name__=="__main__":
#     pytest.main(["test_Login.py"])
    # test_Loginsend()

