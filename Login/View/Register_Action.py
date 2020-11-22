#-*-coding:utf-8-*-#
#--------------------------------------------
#@ProjectName: Study 
#@FileName:Register_Action
#@Author: huangshan
#@Date: 2020/7/11 19:35
#@Description:该模块是用来设置注册接口
#-----------------------------------------------
from django.views import View
import json
from django.http import HttpResponse

class RegsiterActionClass(View):
    @staticmethod
    def judge_isdigit(value):
        return True in map(lambda x: x.isdigit(), value)

    @staticmethod
    def judge_isalpha(value):
        return  True in map(lambda x: x.isalpha(), value)

    def get_message(self,get_info):
        dict1 = {'status': 'success', 'code': 0, "result": get_info}
        dict2 = {'status': '用户长度应为3-15位', 'code': 1, "result": get_info}
        dict3 = {'status': '用户名必须包括数字和字母', 'code': 3, "result": get_info}
        dict4 = {'status': '密码长度应为6-20位', 'code': 4, "result": get_info}
        dict5 = {'status': '密码必须包括数字和字母', 'code': 5, "result": get_info}
        dict6 = {'status': '确认密码与设置的密码不匹配', 'code': 6, "result": get_info}
        return dict1,dict2,dict3,dict4,dict5,dict6

    def get(self, request):
        if request.method == 'GET':
            # 获取输入的用户名
            get_username = request.GET.get("username")
            # 获取输入的密码
            get_password = request.GET.get("password")
            # 获取输入的确认密码
            get_password_confirm = request.GET.get("password_confirm")
            # 将获取到的用户名、密码和确认密码装到一个字典中
            get_info = {"username": get_username, "password": get_password,
                        "password_confirm": get_password_confirm}
            # 判断用户名是否包含数字
            judge_username_member = self.judge_isdigit(get_username)
            # 判断用户名是否包含字母
            judge_username_letter = self.judge_isalpha(get_username)
            # 判断密码是否包含数字
            judge_password_member = self.judge_isdigit(get_password)
            # 判断密码是否包含字母
            judge_password_letter = self.judge_isalpha(get_password)
            # 全部符合
            if len(get_username) >= 3 and len(
                    get_username) <= 15 and judge_username_member and judge_username_letter and len(
                get_password) >= 6 and len(
                get_password) <= 20 and judge_password_member and judge_username_letter and get_password == get_password_confirm:
                return HttpResponse(json.dumps(self.get_message(get_info)[0], ensure_ascii=False))
            # 用户名长度不符合
            elif len(get_username) < 3 or len(get_username) > 15:
                return HttpResponse(json.dumps(self.get_message(get_info)[1], ensure_ascii=False))
            # 用户名内容不符合
            elif judge_username_member == False or judge_username_letter == False:
                return HttpResponse(json.dumps(self.get_message(get_info)[2], ensure_ascii=False))
            # 密码长度不符合
            elif len(get_username) < 6 or len(get_username) > 20:
                return HttpResponse(json.dumps(self.get_message(get_info)[3], ensure_ascii=False))
            # 密码内容不符合
            elif judge_password_member == False or judge_password_letter == False:
                return HttpResponse(json.dumps(self.get_message(get_info)[4], ensure_ascii=False))
            # 两次密码输入不符合
            elif get_password_confirm != get_password:
                return HttpResponse(json.dumps(self.get_message(get_info)[5], ensure_ascii=False))

    def post(self, request):
        if request.method == 'POST':
            # 获取输入的用户名
            get_username = request.POST.get("username")
            # 获取输入的密码
            get_password = request.POST.get("password")
            # 获取输入的确认密码
            get_password_confirm = request.POST.get("password_confirm")
            # 将获取到的用户名、密码和确认密码装到一个字典中
            get_info = {"username": get_username, "password": get_password,
                        "password_confirm": get_password_confirm}
            # 判断用户名是否包含数字
            judge_username_member =self.judge_isdigit(get_username)
            # 判断用户名是否包含字母
            judge_username_letter = self.judge_isalpha(get_username)
            # 判断密码是否包含数字
            judge_password_member = self.judge_isdigit(get_password)
            # 判断密码是否包含字母
            judge_password_letter = self.judge_isalpha(get_password)
            # 全部符合
            if len(get_username) >= 3 and len(
                    get_username) <= 15 and judge_username_member and judge_username_letter and len(
                get_password) >= 6 and len(
                get_password) <= 20 and judge_password_member and judge_username_letter and get_password == get_password_confirm:
                return HttpResponse(json.dumps(self.get_message(get_info)[0],ensure_ascii=False))
            # 用户名长度不符合
            elif len(get_username) < 3 or len(get_username) > 15:
                return HttpResponse(json.dumps(self.get_message(get_info)[1],ensure_ascii=False))
            # 用户名内容不符合
            elif judge_username_member == False or judge_username_letter == False:
                return HttpResponse(json.dumps(self.get_message(get_info)[2],ensure_ascii=False))
            # 密码长度不符合
            elif len(get_username) < 6 or len(get_username) > 20:
                return HttpResponse(json.dumps(self.get_message(get_info)[3],ensure_ascii=False))
            # 密码内容不符合
            elif judge_password_member == False or judge_password_letter == False:
                return HttpResponse(json.dumps(self.get_message(get_info)[4],ensure_ascii=False))
            # 两次密码输入不符合
            elif get_password_confirm != get_password:
                return HttpResponse(json.dumps(self.get_message(get_info)[5],ensure_ascii=False))



