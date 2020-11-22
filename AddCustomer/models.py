from django.db import models

# Create your models here.
from django.db import models
#必须要继承models.Model，不然同步数据会出现问题
class CustomerInfo(models.Model):
    #声明客户类型的选择：
    customer_choice=[("A","A类客户"),("B","B类客户"),("C","C类客户")]
    # name是数据库表中的名称,一般就不需要指定咯，verbose_name是导出Excel或者csv文件时首行的字段说明
    #django会自动生成一个id,如果你不想要这个id，可以自定义一个
    #实在不需要ID的话，则需要指定主键
    customer_name=models.CharField(max_length=12,verbose_name='客户名称',unique=True)
    customer_type=models.CharField(max_length=2,verbose_name='客户分类',choices=customer_choice)
    #IntegerField不需要指定长度
    customer_phone=models.CharField(max_length=11,verbose_name='手机号码')
    customer_mail=models.CharField(max_length=20,verbose_name='电子邮箱')
    customer_address=models.CharField(max_length=100,verbose_name='详细地址',null=False)