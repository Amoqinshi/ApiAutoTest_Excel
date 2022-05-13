# !/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：ApiAutoTest
@File ：Conf.py
@Author ：琴师
@Date ：2022/5/4 8:53 下午
'''
import os
from utils.YamlUtil import YamlReader


file = os.path.abspath(__file__)
# 获取当前项目绝对路径
BASE_DIR = os.path.dirname(os.path.dirname(file))
# 获取config文件所在目录
config_path = BASE_DIR + os.sep + "config"
# 获取conf.yml文件所在目录
config_file = os.path.dirname(file) + os.sep + "conf.yml"
# 获取db.yml文件所在目录
db_config_file = os.path.dirname(file) + os.sep + "db_conf.yml"
# 获取测试用例文件data所在目录
case_file = BASE_DIR + os.sep + "data"
# 获取logs文件所在目录
log_path = BASE_DIR + os.sep+"logs"
# 获取report目录所在路径
report_path = BASE_DIR + os.sep + "report"

def get_report_path():
    """
    获取report绝对路径
    :return:
    """
    return report_path

def get_config_path():
    return config_path


def get_config_file():
    return config_file

def get_log_path():
    """
    :获取Log文件
    """
    return log_path

def get_db_config_file():
    """
    :获取数据库配置文件所在目录
    """
    return db_config_file

def get_caselist_path():
    return case_file

class ConfigYaml():

    def __init__(self):
        # 初始化yaml，读取配置文件
        self.config = YamlReader(get_config_file()).reader()
        self.db_conf = YamlReader(get_db_config_file()).reader()

    def get_excel_file(self):
        return self.config.get("BASE").get("CaseFile")

    def get_conf_UmsTestUrl(self):
        """
        : 获取ums测试环境登陆地址
        """
        return self.config.get("BASE").get("UmsLogin").get("Test")

    def get_conf_UmsReleaseUrl(self):
        """
        : 获取ums预发境登陆地址
        """
        return self.config.get("BASE").get("UmsLogin").get("Release")

    def get_conf_UmsProdUrl(self):
        """
        : 获取ums生产环境登陆地址
        """
        return self.config.get("BASE").get("UmsLogin").get("Prod")

    def get_conf_FzTestUrl(self):
        """
        : 获取方舟服务测试环境地址
        """
        return self.config.get("BASE").get("FzService").get("Test")

    def get_conf_FzReleaseUrl(self):
        """
        : 获取方舟服务预发环境地址
        """
        return self.config.get("BASE").get("FzService").get("Release")

    def get_conf_FzProdUrl(self):
        """
        : 获取方舟服务生产环境地址
        """
        return self.config.get("BASE").get("FzService").get("Prod")

    def get_conf_LogExtension(self):
        """
        : 获取log文件扩展名
        """
        return self.config.get("BASE").get("LogExtension")

    def get_conf_LogLevel(self):
        """
        : 获取log日志等级
        """
        return self.config.get("BASE").get("LogLevel")

    def get_conf_db(self,DB_type):
        """
        :获取数据库配置信息
        """
        return self.db_conf.get(DB_type)

    def get_email_info(self):
        return self.config.get("Email")



if __name__ == "__main__":
    # print(ConfigYaml().get_conf_LogLevel())
    # print(ConfigYaml().get_conf_LogExtension())
    # print(log_path)
    # print(ConfigYaml().get_db_conf("DB_Test"))
    # print(ConfigYaml().get_db_conf("DB_Release"))
    print(ConfigYaml().get_email_info())
    # pass



