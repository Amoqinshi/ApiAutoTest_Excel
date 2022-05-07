# !/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：ApiAutoTest
@File ：YamlUtil.py
@Author ：琴师
@Date ：2022/5/4 8:12 下午
'''
import os
import yaml


class YamlReader(object):
    def __init__(self, yaml_file):
        if os.path.exists(yaml_file):
            self.yaml_file = yaml_file
        else:
            raise FileNotFoundError("文件不存在")
        self._reader = None
        self._reader_all = None

    def reader(self):
        """
        : 第一次调用reader，读取yaml单个文件，如果不是，直接返回之前保存的值
        """
        if not self._reader:
            with open(self.yaml_file, "r+", encoding="utf-8") as f:
                self._reader = yaml.safe_load(f)
        return self._reader

    def reader_all(self):
        """
        : 读取yaml多个文件的方法
        """
        if not self._reader_all:
            with open(self.yaml_file, "r+", encoding="utf-8") as f:
                self._reader_all = list(yaml.safe_load_all(f))
        return self._reader_all


if __name__ == "__main__":
    # A =YamlReader("/Users/hengye/PycharmProjects/ApiAutoTest/data/test_Login.yml")
    # print(A.reader_all())
    # print(A.reader())
    pass