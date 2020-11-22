#-*-coding:utf-8-*-#
#--------------------------------------------
#@ProjectName: Study 
#@FileName:Get_CustromerInfo
#@Author: huangshan
#@Date: 2020/7/15 11:10
#@Description:从页面上获取接口的数据
#-----------------------------------------------
def get_customerinfo(method_obj):
    get_page_info = {
        "customer_name": method_obj.get("customer_name"),
        "customer_type": method_obj.get("customer_type"),
        "customer_phone": method_obj.get("customer_phone"),
        "customer_mail": method_obj.get("customer_mail"),
        "customer_address": method_obj.get("customer_address")
    }
    return get_page_info

def get_query_page_info( method_obj):
    get_page_info = {
        "customer_name": method_obj.get("customer_name"),
        "is_exact":method_obj.get("is_exact")
    }
    return get_page_info

def get_delete_page_info(method_obj):
    get_page_info = {
        "customer_name": method_obj.get("customer_name")
    }
    return get_page_info

