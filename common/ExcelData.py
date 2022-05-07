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

class CaseData(object):
    """
     获取excel文件测试用例
    """
    def __init__(self,testcase):
        self.excel = ExcelReader(testcase)

    def get_run_case(self):
        """
        :return 获取可运行的用例
        """
        run_list = list()
        for line in self.excel.data():

            if  str(line.get(ExcelDataConfig.caseIsRun)).lower() == "y":
                run_list.append(line)
        return run_list