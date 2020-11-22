#-*-coding:utf-8-*-#
#--------------------------------------------
#@ProjectName: Study 
#@FileName:Conn_Sqlite
#@Author: huangshan
#@Date: 2020/7/12 19:48
#@Description:该模块是用封装连接sqlite3数据库
#-----------------------------------------------
from InterfacePorgram.settings import  BASE_DIR
import sqlite3

class ConnSqlite(object):
    def __init__(self):
        self.conn = sqlite3.connect(BASE_DIR + "/AddUser/Modle/test.db")
        self.cursor = self.conn.cursor()

    # 读取数据的方法
    def read_data(self, str_sql):
        self.cursor.execute(str_sql)
        get_reuslt = self.cursor.fetchall()
        return get_reuslt

    #插入数据的方法
    def insert_data(self,str_sql):
        self.cursor.execute(str_sql)
        self.conn.commit()



if __name__ == '__main__':
    print(BASE_DIR + "/AddUser/Modle/test.db")
    conn = ConnSqlite()
    str_sql1 = "select * from  user where username='huangshan002' "
    print(conn.read_data(str_sql1))






