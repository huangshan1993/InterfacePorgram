#-*-coding:utf-8-*-#
#--------------------------------------------
#@ProjectName: Study 
#@FileName:JudgeMethod
#@Author: huangshan
#@Date: 2020/7/15 11:23
#@Description:判断的一些方法封装
#-----------------------------------------------
import re
class JudgeMethod():
    @staticmethod
    def judge_isdigit(value):
        if value.strip().isdigit():
            return True
        else:
            return False

    # 判断是否为133/187/188/189开头
    @staticmethod
    def judge_head(value):
        if re.match(r"^133", value) or re.match(r"^18[7,8,9]", value):
            return True
        else:
            return False

    # 判断是否为163.com或者qq.com结尾
    @staticmethod
    def judge_tail(value):
        if re.match(r"[0-9a-zA-Z_]{0,13}@163.com", value) or re.match(r"[0-9a-zA-Z_]{0,13}@qq.com", value):
            return True
        else:
            return False



