#-*-coding:utf-8-*-#
#--------------------------------------------
#@ProjectName: Study 
#@FileName:Login_Index
#@Author: huangshan
#@Date: 2020/7/11 15:16
#@Description:
#-----------------------------------------------
#使用函数的话，必须传入一个参数，为请求对象
from django.http import HttpResponse  #响应对象
from django.shortcuts import redirect,render
from django.views import View
def LoginIndex(request):
    #实现响应处理
   return  render(request,"Login_Index.html")

class LoginIndexClass(View):
    def get(self,request):
        return HttpResponse("这是get方法")
    def post(self,request):
        return HttpResponse("这是post方法")
