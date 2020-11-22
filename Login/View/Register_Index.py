#-*-coding:utf-8-*-#
#--------------------------------------------
#@ProjectName: Study 
#@FileName:Register_Index
#@Author: huangshan
#@Date: 2020/7/11 19:52
#@Description:
#-----------------------------------------------
from django.shortcuts import render
def RegisterIndex(request):
    # render表示重定向静态页面
   return render(request,"Register_Index.html")