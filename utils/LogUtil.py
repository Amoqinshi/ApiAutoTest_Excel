# !/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：ApiAutoTest 
@File ：LogUtil.py
@Author ：琴师
@Date ：2022/5/5 9:37 上午 
'''
import logging
import datetime
import os
from config import Conf
from  config.Conf import ConfigYaml
from utils.YamlUtil import YamlReader


log_dict = {
    "info": logging.INFO,
    "debug": logging.DEBUG,
    "warning": logging.WARNING,
    "error": logging.ERROR
}


class Logger(object):
    """
    日志打印类
    """
    def __init__(self,log_file,case_desc,log_name,log_level):
        self.now_time = datetime.datetime.now().strftime("%Y%m%d%H%M")
        self.log_file = log_file
        self.case_desc = case_desc
        self.log_name = log_name
        self.log_level = log_level
        # 初始化创建一个logger对象,设置logger名称
        self.logger = logging.getLogger(self.log_name)

        # 设置log级别
        self.logger.setLevel(log_dict[self.log_level])

        # 判断handle是否存在
        if not self.logger.handlers:

            # 创建一个向屏幕输出的handler对象
            Sh_stream = logging.StreamHandler()
            Sh_stream.setLevel(log_dict[self.log_level])
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            Sh_stream.setFormatter(formatter)

            # 创建一个向文件输入的handler对象
            # log_path = os.path.dirname(__file__)
            # log_file = os.path.join(log_path, "%s--%s_log" % ("APPCase", self.now_time))
            Fh_stream = logging.FileHandler(self.log_file, mode="a+", encoding="utf-8")
            Fh_stream.setLevel(log_dict[self.log_level])
            Fh_stream.setFormatter(formatter)


            # 定义日志输出格式

            # 添加handler
            self.logger.addHandler(Sh_stream)
            self.logger.addHandler(Fh_stream)

    #
    # def log_info(self):
    #     # 设置日志配置信息，包括输出格式和日志级别(需求要在开头设置，在中间设置无效)
    #     # logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')




# 获取log目录
log_path = Conf.get_log_path()
# 获取当前时间
current_time = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M")
# 扩展名
log_extension = ConfigYaml().get_conf_LogExtension()
# 组装log文件名称
log_file = os.path.join(log_path,current_time+log_extension)
log_level = ConfigYaml().get_conf_LogLevel()
# 获取用例描述
# case_desc = YamlReader().get_caselist_path()
# print(case_desc)


def my_log(case_desc=None,log_name=None):
    return Logger(log_file=log_file,case_desc=case_desc,log_name=log_name,log_level=log_level).logger


if __name__=="__main__":
    pass