# !/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：ApiAutoTest 
@File ：test_Login.py
@Author ：琴师
@Date ：2022/5/4 4:01 下午 
'''
import os,json
from utils.RequestsUtil import RequestLogic
from utils.YamlUtil import YamlReader
from utils.AssertUtil import Assert
from utils.LogUtil import my_log
from config.Conf import ConfigYaml
from common.ExcelData import CaseData
from common import ExcelConfig
from config import Conf
from common import Base
import pytest


case_file = os.path.join(Conf.get_caselist_path(),ConfigYaml().get_excel_file())
# sheet_name = ConfigYaml.
# 初始化excel文件用例
# case_init = CaseData(case_file)
# 获取全部测试用例 <common.ExcelData.CaseData object at 0x7fdc8ad0e490>,<__main__.CaseData object at 0x7f85878ca670>
all_case = CaseData(case_file).get_all_case()
# 获取可运行测试用例列表
run_list = CaseData(case_file).get_run_case()
# 初始化dataconfig
data_key = ExcelConfig.ExcelDataConfig


class TestLogin(object):

    def setup_class(self):
        self.Log = my_log(log_name=os.path.basename(__file__))
        self.request = RequestLogic()

    def run_api(self,url,method,data=None,headers=None):
        """
        发送请求api
        :return:
        """
        if method == "GET":
            self.Log.info("request data：%s" % (str(data)))
            response_json = self.request.request_get(url=url, data=data, headers=headers)
            self.Log.info("response data：%s" % (str(response_json)))
        else:
            self.Log.info("request data：%s" % (str(data)))
            response_json = self.request.request_post(url=url,data=data, headers=headers)
            self.Log.info("response data：%s" % (str(response_json)))
        return response_json

    def run_pre(self,pre_case):
        """
        执行前置用例
        :param pre_case:
        :return:
        """
        if pre_case.get(data_key.caseId) == "Login":
            url = ConfigYaml().get_conf_UmsTestUrl() + pre_case.get(data_key.caseUrl)
        else:
            url = ConfigYaml().get_conf_FzTestUrl() + pre_case.get(data_key.caseUrl)
        data = pre_case.get(data_key.caseParams)
        headers = Base.json_parse(pre_case.get(data_key.caseHeaders))
        method = pre_case.get(data_key.caseMethod)
        res = self.run_api(url,method,data=data,headers=headers)
        return res


    @pytest.mark.parametrize("case",run_list)
    def test_run(self,case):

        pre = case.get(data_key.casePre)
        data = case.get(data_key.caseParams)
        headers = case.get(data_key.caseHeaders)
        method = case.get(data_key.caseMethod)
        expect = case.get(data_key.caseExpect)
        if case.get(data_key.caseId) == "Login":
            url = ConfigYaml().get_conf_UmsTestUrl() + case.get(data_key.caseUrl)
        else:
            url = ConfigYaml().get_conf_FzTestUrl() + case.get(data_key.caseUrl)
        if pre:
            # 获取前置测试用例
            pre_case = CaseData(case_file).get_case_pre(pre)
            prse = self.run_pre(pre_case)

        headers1 = self.get_creat_relation(headers,prse)
        res = self.run_api(url,method,data=data,headers= Base.json_parse(headers1))
        Assert.assert_in_body(res["body"]["ums_user"],expect)
        # print("正常用例执行",res)

    def get_creat_relation(self,headers,pre_case_result):
        """
        参数关联
        :param headers:
        :param pre_case_result:
        :return:
        """
        headers_para = Base.data_find(headers)
        if len(headers_para) > 0:
            headers_data = pre_case_result.get("body").get("access_token")
            headers = Base.res_sub(str(headers),headers_data)
        return headers


if __name__=="__main__":
    pytest.main(["-s","test_Login11.py"])
    # pass
    # print(TestLogin().get_creat_relation(headers={"authorization":"Bearer ${token}$","x-business-id":"1","x-channel-id":"8"},pre_case_result={'code': 200, 'body': {'is_new': False, 'user_id': 706691603, 'access_token': 'eyJ0eXAiOiJqd3QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJ1bXMiLCJzdWIiOjcwNjY5MTYwMywiYXVkIjoiZ2FvZGluZ3giLCJleHAiOjE2NTI0Mjg5MTAsImp0aSI6IjIzZTU4ZDhiZjU4YzhkNTMxOGRmNTk5YWM0NDM0MzE2OWI1MGQ5NDAifQ.iOnf-sMJ8EBuOnyJCDTseFgM-EtftrY0EDRLeajd_a4', 'refresh_token': '5e04c8005f00fa669d99a8f2b0abcfb1eb506be5', 'access_token_expires_at': '2022-05-13T08:01:50.000Z', 'refresh_token_expires_at': '2022-05-27T08:01:50.046Z', 'access_token_life_time': 86400, 'refresh_token_life_time': 1296000}}))



