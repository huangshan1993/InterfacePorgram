#-*-coding:utf-8-*-#
#--------------------------------------------
#@ProjectName: Study 
#@FileName:CheckData
#@Author: huangshan
#@Date: 2020/7/15 21:24
#@Description:一些逻辑判断的封装
#-----------------------------------------------
from Public.Get_CustromerInfo import get_customerinfo
class Check_Data():
    def __init__(self,method_obj):
        self.get_page_info=get_customerinfo(method_obj)

    # 判断所有必传参数是是否有传
    def judge_allpars_notNone(self):
        if self.get_page_info["customer_name"] != None and self.get_page_info["customer_type"] != None and self.get_page_info[
            "customer_phone"] != None and self.get_page_info["customer_mail"] != None:
            return True
        else:
            return False

    # 判断所有必填参数的值是否为空
    def judge_allpars_Null(self):
        if self.get_page_info["customer_name"] == '' and self.get_page_info["customer_type"] == '' and self.get_page_info[
            "customer_phone"] == '' and self.get_page_info["customer_mail"] == '':
            return True
        else:
            return False

    def judge_comseter_type(self):
        if self.get_page_info["customer_type"] not in ["A", "B", "C"]:
            return True
        else:
            return False



