#-*-coding:utf-8-*-#
#--------------------------------------------
#@ProjectName: Study 
#@FileName:AddUser_Action
#@Author: huangshan
#@Date: 2020/7/12 19:47
#@Description:该模块是用来封装增加用户的接口
#-----------------------------------------------
from django.views import View
from django.http import HttpResponse
from AddUser.Modle.Conn_Sqlite import ConnSqlite
import re
import json
class  Adduser(View):
    #判断是否为数字
    @staticmethod
    def judge_isdigit(value):
        if value.strip().isdigit():
           return True
        else:
            return False
    #判断是否为133/187/188/189开头
    @staticmethod
    def judge_head(value):
        if re.match(r"^133",value) or re.match(r"^18[7,8,9]",value):
            return True
        else:
            return False
    #判断是否为163.com或者qq.com结尾
    @staticmethod
    def judge_tail(value):
        if re.match(r"[0-9a-zA-Z_]{0,13}@163.com",value) or re.match(r"[0-9a-zA-Z_]{0,13}@qq.com",value):
            return True
        else:
            return False
    #获取数据库test.db中user表的数据
    def get_database(self,username):
        conn = ConnSqlite()
        str_sql = "select * from user where username='%s'" % username
        return conn.read_data(str_sql)
    #调用插入数据库的方法
    def get_insert_data(self,username,usertype,linkman,mobile,mail,address):
        conn = ConnSqlite()
        str_sql="insert into user values('%s','%s','%s','%s','%s','%s')"%(username,usertype,linkman,mobile,mail,address)
        return conn.insert_data(str_sql)
    #从页面上获取数据,并封装在一个方法中
    def get_userinfo(self,method_obj):
        get_username=method_obj.get("username")
        get_usertype=method_obj.get('usertype')
        get_linkman=method_obj.get('linkman')
        get_mobile=method_obj.get('mobile')
        get_mail=method_obj.get('mail')
        get_address=method_obj.get('address')
        return {"username":get_username,"usertype":get_usertype,"linkman":get_linkman,"mobile":get_mobile,"mail":get_mail,"address":get_address}
   #接口参数逻辑处理的方法
    def compare_data(self,method_obj):
        get_page_info=self.get_userinfo(method_obj)
        get_database_info=self.get_database(get_page_info["username"])
        #print("获取的页面信息：",get_page_info)
        return_reuslt={"reason": [],"result": [],"error_code":[]}

        if get_page_info["username"]!=None and get_page_info["usertype"]!=None  and get_page_info["linkman"]!=None and get_page_info["mobile"] !=None and get_page_info["mail"]!=None:
            if get_page_info["username"] == '' and get_page_info["usertype"] == '' and get_page_info[
                "linkman"] == '' and get_page_info["mobile"] == '' and get_page_info["mail"] == '':
                return_reuslt["reason"] = "客户名称、客户分类、联系人、手机号码和电子邮箱不能为空"
                return_reuslt["error_code"] = 2013
            elif len(get_database_info) >= 1:
                return_reuslt["reason"] = "数据库中已存在同名的客户"
                return_reuslt["error_code"] = 2000
            elif get_page_info["username"] == '':
                return_reuslt["reason"] = "请填写客户名称"
                return_reuslt["error_code"] = 2001
            elif len(get_page_info["username"]) < 6 or len(get_page_info["username"]) > 12:
                return_reuslt["reason"] = "客户名称的长度必须为6-12个字符"
                return_reuslt["error_code"] = 2002
            elif get_page_info["usertype"] == '':
                return_reuslt["reason"] = "请填写客户分类"
                return_reuslt["error_code"] = 2003
            elif get_page_info["usertype"] not in ["A", "B", "C"]:
                return_reuslt["reason"] = "客户分类不存在"
                return_reuslt["error_code"] = 2004
            elif get_page_info["linkman"] == '':
                return_reuslt["reason"] = "请填写联系人"
                return_reuslt["error_code"] = 2005
            elif len(get_page_info["linkman"]) < 6 or len(get_page_info["linkman"]) > 12:
                return_reuslt["reason"] = "联系人的长度必须为6-12个字符"
                return_reuslt["error_code"] = 2006
            elif get_page_info["mobile"] == '':
                return_reuslt["reason"] = "请填写手机号码"
                return_reuslt["error_code"] = 2007
            elif len(get_page_info["mobile"]) != 11:
                return_reuslt["reason"] = "手机号码的长度必须为11位"
                return_reuslt["error_code"] = 2008
            elif self.judge_isdigit(get_page_info["mobile"]) ==False:
                return_reuslt["reason"] = "手机号码只能为数字"
                return_reuslt["error_code"] = 2009
            elif self.judge_head(get_page_info["mobile"]) == False:
                return_reuslt["reason"] = "手机号码只能以133/187/188/189开头"
                return_reuslt["error_code"] = 2010
            elif get_page_info["mail"] == '':
                return_reuslt["reason"] = "请填写电子邮箱"
                return_reuslt["error_code"] = 2011
            elif self.judge_tail(get_page_info["mail"]) == False:
                return_reuslt["reason"] = "电子邮箱只能为QQ或者163邮箱"
                return_reuslt["error_code"] = 2012
            else:
                self.get_insert_data(get_page_info["username"], get_page_info["usertype"], get_page_info["linkman"],
                                     get_page_info["mobile"], get_page_info["mail"], get_page_info["address"])
                return_reuslt["reason"] = "sucess"
                return_reuslt["result"] = get_page_info
                return_reuslt["error_code"] = 0
            return return_reuslt
        elif get_page_info["username"]==None:
            return_reuslt["reason"] = "缺少客户名称参数"
            return_reuslt["error_code"] = 2014
        elif get_page_info["usertype"]==None:
            return_reuslt["reason"] = "缺少客户分类参数"
            return_reuslt["error_code"] = 2015
        elif get_page_info["linkman"] == None:
            return_reuslt["reason"] = "缺少联系人参数"
            return_reuslt["error_code"] = 2016
        elif get_page_info["mobile"] == None:
            return_reuslt["reason"] = "缺少手机号码参数"
            return_reuslt["error_code"] = 2017
        elif get_page_info["mail"] == None:
            return_reuslt["reason"] = "缺少电子邮箱参数"
            return_reuslt["error_code"] = 2018
        return return_reuslt

    def get(self,request):
        return HttpResponse(json.dumps(self.compare_data(request.GET),ensure_ascii=False))

    def post(self,request):
        return HttpResponse(json.dumps(self.compare_data(request.POST),ensure_ascii=False))




