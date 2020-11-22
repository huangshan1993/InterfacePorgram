from Public.Get_CustromerInfo import get_customerinfo,get_query_page_info,get_delete_page_info
from django.http import HttpResponse
from AddCustomer.models import CustomerInfo
import json
from Public.JudgeMethod import JudgeMethod
from Public.CheckData import Check_Data
from Public.ResponseData import ResponseData

#新增客户的接口
def add_customer(request):
    ju=Check_Data(request.POST)
    get_page_info=get_customerinfo(request.POST)
    get_database_info= CustomerInfo.objects.filter(customer_name=get_page_info['customer_name'])
    if ju.judge_allpars_notNone()==True:
        if ju.judge_allpars_Null()==True:
            return HttpResponse(json.dumps(ResponseData.get_message_one(), ensure_ascii=False))
        elif len(get_database_info) >= 1:
            return HttpResponse(json.dumps(ResponseData.get_message_two(), ensure_ascii=False))
        elif get_page_info["customer_name"] == '':
            return HttpResponse(json.dumps(ResponseData.get_message_three(), ensure_ascii=False))
        elif len(get_page_info["customer_name"]) < 6 or len(get_page_info["customer_name"]) > 12:
            return HttpResponse(json.dumps(ResponseData.get_message_four(), ensure_ascii=False))
        elif get_page_info["customer_type"] == '':
            return HttpResponse(json.dumps(ResponseData.get_message_five(), ensure_ascii=False))
        elif  ju.judge_comseter_type()==True:
            return HttpResponse(json.dumps(ResponseData.get_message_six(), ensure_ascii=False))
        elif get_page_info["customer_phone"] == '':
            return HttpResponse(json.dumps(ResponseData.get_message_seven(), ensure_ascii=False))
        elif len(get_page_info["customer_phone"]) != 11:
            return HttpResponse(json.dumps(ResponseData.get_message_eight(), ensure_ascii=False))
        elif JudgeMethod.judge_isdigit(get_page_info["customer_phone"]) == False:
            return HttpResponse(json.dumps(ResponseData.get_message_nine(), ensure_ascii=False))
        elif JudgeMethod.judge_head(get_page_info["customer_phone"]) == False:
            return HttpResponse(json.dumps(ResponseData.get_message_ten(), ensure_ascii=False))
        elif get_page_info["customer_mail"] == '':
            return HttpResponse(json.dumps(ResponseData.get_message_eleven(), ensure_ascii=False))
        elif JudgeMethod.judge_tail(get_page_info["customer_mail"]) == False:
            return HttpResponse(json.dumps(ResponseData.get_message_twelve(), ensure_ascii=False))
        else:
            CustomerInfo.objects.create(**get_page_info)
        return HttpResponse(json.dumps(ResponseData.get_message_twentytwo(get_page_info), ensure_ascii=False))
    elif get_page_info["customer_name"] == None:
        return HttpResponse(json.dumps(ResponseData.get_message_thirteen(), ensure_ascii=False))
    elif get_page_info["customer_type"] == None:
        return HttpResponse(json.dumps(ResponseData.get_message_fourteen(), ensure_ascii=False))
    elif get_page_info["customer_phone"] == None:
        return HttpResponse(json.dumps(ResponseData.get_message_fiveteen(), ensure_ascii=False))
    elif get_page_info["customer_mail"] == None:
        return HttpResponse(json.dumps(ResponseData.get_message_sixteen(),ensure_ascii=False))

#修改客户的接口
def update_customer(request):
    ju = Check_Data(request.POST)
    get_page_info = get_customerinfo(request.POST)
    get_customer_name= CustomerInfo.objects.filter(customer_name=get_page_info['customer_name'])
    if get_page_info['customer_name']!=None:
        if len(get_customer_name) == 1:
            customer = CustomerInfo.objects.get(customer_name=get_page_info['customer_name'])
            if get_page_info['customer_type']!=None:

                if get_page_info['customer_type']=='':
                    return HttpResponse(json.dumps(ResponseData.get_message_five(), ensure_ascii=False))
                elif ju.judge_comseter_type() == True:
                    return HttpResponse(json.dumps(ResponseData.get_message_six(), ensure_ascii=False))
                else:
                    customer.customer_type = get_page_info['customer_type']
                    customer.save()
                    return HttpResponse(json.dumps(ResponseData.get_message_eighteen(), ensure_ascii=False))
            elif get_page_info['customer_phone']!=None:
                if get_page_info["customer_phone"] == '':
                    return HttpResponse(json.dumps(ResponseData.get_message_seven(), ensure_ascii=False))
                elif len(get_page_info["customer_phone"]) != 11:
                    return HttpResponse(json.dumps(ResponseData.get_message_eight(), ensure_ascii=False))
                elif JudgeMethod.judge_isdigit(get_page_info["customer_phone"]) == False:
                    return HttpResponse(json.dumps(ResponseData.get_message_nine(), ensure_ascii=False))
                elif JudgeMethod.judge_head(get_page_info["customer_phone"]) == False:
                    return HttpResponse(json.dumps(ResponseData.get_message_ten(), ensure_ascii=False))
                else:
                    customer.customer_phone = get_page_info['customer_phone']
                    customer.save()
                    return HttpResponse(json.dumps(ResponseData.get_message_eighteen(), ensure_ascii=False))
            elif get_page_info['customer_mail'] != None:
                if get_page_info["customer_mail"] == '':
                    return HttpResponse(json.dumps(ResponseData.get_message_eleven(), ensure_ascii=False))
                elif JudgeMethod.judge_tail(get_page_info["customer_mail"]) == False:
                    return HttpResponse(json.dumps(ResponseData.get_message_twelve(), ensure_ascii=False))
                else:
                    customer.customer_mail = get_page_info['customer_mail']
                    customer.save()
                    return HttpResponse(json.dumps(ResponseData.get_message_eighteen(), ensure_ascii=False))
            elif get_page_info['customer_address'] != '':
                customer.customer_address = get_page_info['customer_address']
                customer.save()
                return HttpResponse(json.dumps(ResponseData.get_message_eighteen(), ensure_ascii=False))
        else:
            return HttpResponse(json.dumps(ResponseData.get_message_nineteen(), ensure_ascii=False))
    else:
        return HttpResponse(json.dumps(ResponseData.get_message_thirteen(), ensure_ascii=False))

#查询用户的接口
def select_customer(request):
    get_page_info = get_query_page_info(request.POST)
    if get_page_info['customer_name'] != None:
        if get_page_info['customer_name']!='':
            #精确查询
            if get_page_info['is_exact'] == None or int(get_page_info['is_exact'])== 0:
                get_customer_name = CustomerInfo.objects.filter(customer_name=get_page_info['customer_name'])
                if len(get_customer_name) >= 1:
                    list1 = []
                    for value in get_customer_name.values():
                        list1.append(value)
                    total = get_customer_name.count()
                    return HttpResponse(json.dumps(ResponseData.get_message_seventeen(total, list1), ensure_ascii=False))
                else:
                    return HttpResponse(json.dumps(ResponseData.get_message_twentyone(), ensure_ascii=False))
            #模糊查询
            elif int(get_page_info['is_exact']) == 1:
                get_customer_name=CustomerInfo.objects.filter(customer_name__contains=get_page_info['customer_name'])
                print(get_customer_name)
                if len(get_customer_name) >= 1:
                    list1 = []
                    for value in get_customer_name.values():
                        list1.append(value)
                    total = get_customer_name.count()
                    return HttpResponse(json.dumps(ResponseData.get_message_seventeen(total, list1), ensure_ascii=False))
                else:
                    return HttpResponse(json.dumps(ResponseData.get_message_twentyone(), ensure_ascii=False))
            else:
                return HttpResponse(json.dumps(ResponseData.get_message_twentythree(), ensure_ascii=False))

        else:
            # 客户名称为空
            return HttpResponse(json.dumps(ResponseData.get_message_three(), ensure_ascii=False))
    else:
        list2=[]
        for value in  CustomerInfo.objects.all():
            dict1=({"id":value.id,"customer_name":value.customer_name,"customer_type":value.customer_type,"customer_phone":value.customer_phone,"customer_mail":value.customer_mail,"customer_address":value.customer_address})
            list2.append(dict1)
        total=CustomerInfo.objects.all().count()
        return HttpResponse(json.dumps(ResponseData.get_message_seventeen(total,list2), ensure_ascii=False))


#删除客户的接口
def delete_customer(request):
    get_page_info = get_delete_page_info(request.POST)
    get_customer_name = CustomerInfo.objects.filter(customer_name=get_page_info['customer_name'])
    if get_page_info['customer_name'] != None:
        if len(get_customer_name) == 1:
            customer = CustomerInfo.objects.get(customer_name=get_page_info['customer_name'])
            customer.delete()
            return HttpResponse(json.dumps(ResponseData.get_message_twenty(), ensure_ascii=False))
        else:
            return HttpResponse(json.dumps(ResponseData.get_message_nineteen(), ensure_ascii=False))
    else:
        return HttpResponse(json.dumps(ResponseData.get_message_thirteen(), ensure_ascii=False))


















