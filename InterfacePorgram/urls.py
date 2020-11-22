"""InterfacePorgram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Login.View.Login_Index import LoginIndex,LoginIndexClass
from Login.View.Login_Action import LoginActionClass
from Login.View.Register_Index import RegisterIndex
from Login.View.Register_Action import RegsiterActionClass
from AddUser.View.AddUser_Action import Adduser
from AddCustomer.views import add_customer,update_customer,delete_customer,select_customer
from CustomerManage.views import add_custo,update_custo,delete_custo,select_custo


urlpatterns = [
    path('admin/', admin.site.urls),
    path('loginIndex/', LoginIndex),
    path('loginIndexClass/',LoginIndexClass.as_view()),
    path('loginAction/',LoginActionClass.as_view()),
    #get方法的路径
    # path('registerIndex/',RegisterIndex),
    # path('registerAction/',RegsiterActionClass.as_view())
    #post方法的路径
    path('registerIndex', RegisterIndex),
    path('registerAction', RegsiterActionClass.as_view()),
    path('addUser', Adduser.as_view()),
    path('addCustomer',add_customer),
    path('queryCustomer',select_customer),
    path('updateCustomer',update_customer),
    path('deleteCustomer',delete_customer)
]


