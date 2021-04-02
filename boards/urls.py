# *_* coding: utf-8 *_*
# time:2021-04-0214:08
# tools:PyCharm
# file_name：urls.py

# 停下休息的时候不要忘记别人还在奔跑！！！
#
#
from django.urls import path,include
from boards import views as boards_view
urlpatterns = [

    path('',boards_view.home,name='home'),




    ]