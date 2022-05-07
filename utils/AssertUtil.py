# !/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：ApiAutoTest 
@File ：AssertUtil.py
@Author ：琴师
@Date ：2022/5/5 1:44 下午 
'''
import json
from utils.LogUtil import my_log

class Assert(object):
    """
    封装断言类
    """
    def __init__(self):
        self.log = my_log("Assert123")

    def  assert_code(self,code,expect_code):
        """
         断言返回状态码
        :param code:
        :param expect_code:
        :return:
        """
        try:
            assert int(code) == int(expect_code)
            return True
        except Exception as  e:
            self.log.error("code error, code is {}, expect_code is {}".format(code,expect_code))
            raise e

    def  assert_body(self,body,expect_body):
        """
        断言返回内容相等
        :param body:
        :param expect_body:
        :return:
        """
        try:
            assert body == expect_body
            return True
        except Exception as e:
            self.log.error("body error, body is {}, expect_body is {}".format(body,expect_body))
            raise  e

    def  assert_in_body(self,body,expect_body):
        """
        断言返回内容是否包含期望内容
        :param body:
        :param expect_body:
        :return:
        """
        try:
            body = json.dump(body)
            assert expect_body in body
            return True
        except Exception as e:
            self.log.error("返回内容不包含期望内容".format(body,expect_body))
            raise  e


