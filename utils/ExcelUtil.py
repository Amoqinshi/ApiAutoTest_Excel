# !/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：ApiAutoTest 
@File ：ExcelUtil.py
@Author ：琴师
@Date ：2022/5/6 10:17 上午 
'''

import os
import xlrd


class ExcelReader():

    def __init__(self,file_path):
        if  os.path.exists(file_path):
            self.excel_file = file_path
            self.case = list()
        else:
            raise FileNotFoundError("文件不存在")


    def data(self):
        workbook = xlrd.open_workbook(self.excel_file)
        sheet = workbook.sheet_by_index(0)
        title = sheet.row_values(0)
        for col in range(1, sheet.nrows):
            col_values = sheet.row_values(col)
            self.case.append(dict(zip(title,col_values)))
        return self.case

if __name__=="__main__":
    # excel = ExcelReader("../data/ApiCases.xlsx")
    # print(excel.data())
    pass

