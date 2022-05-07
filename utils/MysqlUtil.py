# !/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：ApiAutoTest
@File ：MysqlUtil.py
@Author ：琴师
@Date ：2022/5/5 2:11 下午
'''
import pymysql
from utils.LogUtil import my_log

# db = pymysql.connect(
#     host="211.103.136.242",
#     user="test",
#     password="test123456",
#     database="meiduo",
#     charset="utf8",
#     port=7090
# )
#
# cursor = db.cursor()
# sql = "select username, password from tb_users"
#
# cursor.execute(sql)
#
# res = cursor.fetchone()
# print(res)


class ConnectDatabase():
    """
    数据库操作类
    """

    def __init__(
            self,
            host,
            user,
            password,
            database,
            charset="utf8",
            port=7090):
        self.connection_Test = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            charset=charset,
            port=port,
            cursorclass=pymysql.cursors.DictCursor
        )
        self.Log = my_log()

    def Select_Sql(self, sql):
        try:
            with self.connection_Test.cursor() as cursor:
                cursor.execute(sql)
                self.connection_Test.commit()
                result = cursor.fetchone()
                return result
        except Exception as e:
            self.connection_Test.rollback()
            self.Log.warn("Mysql 执行失败，{}".format(e))
        finally:
            cursor.close()

    def Select_Sql_All(self, sql):
        try:
            with self.connection_Test.cursor() as cursor:
                cursor.execute(sql)
                self.connection_Test.commit()
                result = cursor.fetchall()
                return result
        except Exception as e:
            self.connection_Test.rollback()
            self.Log.warn("Mysql 执行失败，{}".format(e))
        finally:
            cursor.close()

    def Update_Sql(self, sql):
        try:
            with self.connection_Test.cursor() as cursor:
                cursor.execute(sql)
                self.connection_Test.commit()
                result = cursor.fetchone()
                return result
        except Exception as e:
            self.connection_Test.rollback()
            self.Log.warn("Mysql 执行失败，{}".format(e))
        finally:
            cursor.close()


if __name__ == "__main__":
    SqlEngine = ConnectDatabase(host="211.103.136.242",
                        user="test",
                        password="test123456",
                        database="meiduo",
                        charset="utf8",
                        port=7090)
    #
    res = SqlEngine.Select_Sql(
            sql="select * from tb_users where id='1'")
    print(res)

    # pass