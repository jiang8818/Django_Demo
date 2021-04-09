# *_* coding: utf-8 *_*
# time:2021-04-079:46
# tools:PyCharm
# file_name：urls.py

# 停下休息的时候不要忘记别人还在奔跑！！！
#
#

from django.urls import path,include,re_path
from accounts import views as account_view
from django.contrib.auth import views as auth_views
urlpatterns = [

    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('signup/', account_view.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'),name='login'),



]
