# !/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：ApiAutoTest 
@File ：test_Login.py
@Author ：琴师
@Date ：2022/5/4 4:01 下午 
'''
import requests,yaml,os
from utils.RequestsUtil import RequestLogic
from utils.YamlUtil import YamlReader
from utils.AssertUtil import Assert
from utils.LogUtil import my_log
from config.Conf import ConfigYaml
from common.ExcelData import CaseData
from common import ExcelConfig
from config import Conf
from common.Base import init_db
import pytest,json


case_file = os.path.join(Conf.get_caselist_path(),ConfigYaml().get_excel_file())
# sheet_name = ConfigYaml.
# 获取运行测试用例列表
run_list = CaseData(case_file).get_run_case()


class TestLogin(object):

    def setup_class(self):
        self.Log = my_log(log_name=os.path.basename(__file__))
        self.request = RequestLogic()

    @pytest.mark.parametrize("case",run_list)
    def test_run(self,case):
        data_key = ExcelConfig.ExcelDataConfig
        url =ConfigYaml().get_conf_UmsTestUrl() + case.get(data_key.caseUrl)
        data = case.get(data_key.caseParams)
        self.Log.info("request data：%s" % (str(data)))
        response_json = self.request.request_post(url=url,data=data)
        self.Log.info("response data：%s" % (str(response_json)))





if __name__=="__main__":
    pytest.main(["test_Login11.py"])


