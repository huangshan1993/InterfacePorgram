#-*-coding:utf-8-*-#
#--------------------------------------------
#@ProjectName: Study 
#@FileName:Conn_Sqlite
#@Author: huangshan
#@Date: 2020/7/12 15:03
#@Description:
#-----------------------------------------------
import sqlite3
from InterfacePorgram.settings import BASE_DIR
base=BASE_DIR+"\Modle\mydb.db"
class ConnSqlite(object):
    def __init__(self):
        self.conn=sqlite3.connect(base)
        self.cursor=self.conn.cursor()
    def read_data(self,str_sql):
        self.cursor.execute(str_sql)
        get_result=self.cursor.fetchall()
        return get_result
if __name__ == '__main__':
    conn=ConnSqlite()
    str_sql="select *  from userinfo"
    print(conn.read_data(str_sql))
    base=BASE_DIR+"\Modle\mydb.db"
    print(base)
