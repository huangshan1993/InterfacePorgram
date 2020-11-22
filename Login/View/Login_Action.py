#-*-coding:utf-8-*-#
#--------------------------------------------
#@ProjectName: Study 
#@FileName:Login_Action
#@Author: huangshan
#@Date: 2020/7/11 16:44
#@Description:
#-----------------------------------------------
from django.views import View
from django.http import HttpResponse
import json
class LoginActionClass(View):
    def get(self,request):
        dict1={'status':'success','code':0}
        print("当前的协议：",request)
        return HttpResponse(json.dumps(dict1))
