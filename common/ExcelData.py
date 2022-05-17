# !/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：ApiAutoTest
@File ：ExcelData.py
@Author ：琴师
@Date ：2022/5/6 12:59 下午
'''
from utils.ExcelUtil import ExcelReader
from common.ExcelConfig import ExcelDataConfig

import xlrd

casePre = ExcelDataConfig.casePre


class CaseData(object):
    """
     获取excel文件测试用例
    """

    def __init__(self, testcase):
        self.excel = ExcelReader(testcase)

    def get_run_case(self):
        """
        :return 获取可运行的用例
        """
        run_list = [
            m for m in self.excel.data() if m.get(
                ExcelDataConfig.caseIsRun) == "Y"]
        return run_list

    def get_all_case(self):
        """
         获取全部测试用例
        :return:
        """
        run_list = [line for line in self.excel.data()]
        return run_list

    def get_case_pre(self, pre):
        """
        根据前置条件：从全部测试用例中取到对应的前置测试用例
        :return:
        """
        run_list = self.get_all_case()
        for line in run_list:
            if pre in dict(line).values():
                return line
        return None


# testcase = "../data/ApiCases.xlsx"
# for x in CaseData(testcase).get_run_case():
#     print(x)
# print(CaseData(testcase).get_run_case())
# print("===================================")
# print(CaseData(testcase).get_all_case())

# print(CaseData(testcase).get_case_pre(casePre))
