# !/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：ApiAutoTest
@File ：RequestsUtil.py
@Author ：琴师
@Date ：2022/5/4 3:50 下午
'''
import requests,json
from utils.LogUtil import my_log


class RequestLogic(object):
    """
    请求方法二次封装
    """

    def __init__(self):
        self.log = my_log("Requests")

    def request_api(
            self,
            url,
            data=None,
            params=None,
            headers=None,
            method="GET"):
        if method == "GET":
            r_content = requests.get(url, params=params, headers=headers)
        elif method == "POST":
            r_content = requests.post(url, data=data, headers=headers,verify=False)
        code = r_content.status_code
        try:
            body = r_content.json()
        except Exception as e:
            body = r_content.text
        res = dict()
        res["code"] = code
        res["body"] = body
        return res

    def request_get(self, **kwargs):
        """
        传入请求参数,返回json请求结果
        :param kwargs: json:请求数据, url：请求路径， header:请求头
        :return:
        """
        request_url = kwargs.get("url")
        request_params = kwargs.get("data")
        request_headers = kwargs.get("headers")
        return self.request_api(
            url=request_url,
            params=request_params,
            headers=request_headers)

    def request_post(self, **kwargs):
        """
        传入请求参数,返回json请求结果
        :param kwargs: json:请求数据, url：请求路径， header:请求头
        :return:
        """
        request_url = kwargs.get("url")
        request_headers = kwargs.get("headers")
        request_data = kwargs.get("data")
        # return self.request_api(
        #     url=request_url,
        #     data= json.loads(request_data),
        #     headers=request_headers,
        #     method="POST")
        if isinstance(request_data,dict):
            return self.request_api(
                url=request_url,
                data=json.loads(json.dumps(request_data)),
                headers=request_headers,
                method="POST")
        else:
            return self.request_api(
                url=request_url,
                data=json.loads(str(request_data)),
                headers=request_headers,
                method="POST")


if __name__ == "__main__":
    # A = RequestLogic()
    # print(
    #     A.request_post(
    #         url="https://ums-fat.gaoding.com/connect/oauth/tokens",
    #         data={"grant_type": "password","client_id": "gaodingx","client_secret": "7da458070e57b98e11d00d9286f23537","os": "mac os","mobile_area_code": 86,"mobile": "18218080002","password": "111111"},
    #     ))
    pass
