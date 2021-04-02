# *_* coding: utf-8 *_*
# time:2021-04-0214:14
# tools:PyCharm
# file_name：urls.py

# 停下休息的时候不要忘记别人还在奔跑！！！
#
#


from django.urls import path,include
from hr import views as hr_view
urlpatterns = [

    path('',hr_view.hr_home,name='hr_home'),




    ]