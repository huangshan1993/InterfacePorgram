#-*-coding:utf-8-*-#
#--------------------------------------------
#@ProjectName: Study 
#@FileName:ResponseData
#@Author: huangshan
#@Date: 2020/7/15 22:06
#@Description:响应内容的封装
#-----------------------------------------------
class ResponseData():
    @staticmethod
    def get_message_one():
        return  {"reason": "客户名称、客户分类、联系人、手机号码和电子邮箱不能为空", "result": [], "error_code": 2013}
    @staticmethod
    def get_message_two():
        return {"reason": "数据库中已存在同名的客户", "result": [], "error_code": 2000}
    @staticmethod
    def get_message_three():
        return {"reason": "请填写客户名称", "result": [], "error_code": 2001}

    @staticmethod
    def get_message_four():
        return {"reason": "客户名称的长度必须为6-12个字符", "result": [], "error_code": 2002}

    @staticmethod
    def get_message_five():
        return {"reason": "请填写客户分类", "result": [], "error_code": 2003}

    @staticmethod
    def get_message_six():
        return {"reason": "客户分类不存在", "result": [], "error_code": 2004}

    @staticmethod
    def get_message_seven():
        return {"reason": "请填写手机号码", "result": [], "error_code": 2007}

    @staticmethod
    def get_message_eight():
        return {"reason": "手机号码的长度必须为11位", "result": [], "error_code": 2008}

    @staticmethod
    def get_message_nine():
        return {"reason": "手机号码只能为数字", "result": [], "error_code": 2009}

    @staticmethod
    def get_message_ten():
        return {"reason": "手机号码只能以133/187/188/189开头", "result": [], "error_code": 2010}

    @staticmethod
    def get_message_eleven():
        return {"reason": "请填写电子邮箱", "result": [], "error_code": 2011}

    @staticmethod
    def get_message_twelve():
        return {"reason": "电子邮箱只能为QQ或者163邮箱", "result": [], "error_code": 2012}

    @staticmethod
    def get_message_thirteen():
        return {"reason": "缺少客户名称参数", "result": [], "error_code": 2014}

    @staticmethod
    def get_message_fourteen():
        return {"reason": "缺少客户分类参数", "result": [], "error_code": 2015}

    @staticmethod
    def get_message_fiveteen():
        return {"reason": "缺少手机号码参数", "result": [], "error_code": 2017}

    @staticmethod
    def get_message_sixteen():
        return {"reason": "缺少电子邮箱参数", "result": [], "error_code": 2018}

    @staticmethod
    def get_message_seventeen(total,values):
        return {"reason": "查询成功","total" :total,"result": values, "error_code": 00}

    @staticmethod
    def get_message_eighteen():
        return {"reason": "修改成功",  "error_code": 000000}

    @staticmethod
    def get_message_nineteen():
        return {"reason": "客户名称不存在", "error_code": 100000}

    @staticmethod
    def get_message_twenty():
        return {"reason": "删除成功", "error_code": 0000}

    @staticmethod
    def get_message_twentyone():
        return {"reason": "数据库中不存在该数据", "error_code": 100001}

    @staticmethod
    def get_message_twentytwo( values):
        return {"reason": "新增成功", "result": values, "error_code": 0}

    @staticmethod
    def get_message_twentythree():
        return {"reason": "传入is_exact的值有误", "result":[], "error_code": 0}


