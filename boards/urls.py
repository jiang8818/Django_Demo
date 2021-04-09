# *_* coding: utf-8 *_*
# time:2021-04-0216:47
# tools:PyCharm
# file_name：urls.py

# 停下休息的时候不要忘记别人还在奔跑！！！
#
#

from django.urls import path, include, re_path
from boards import views as boards_view

urlpatterns = [

    path('', boards_view.boards_home, name='boards_home'),
    # re_path(r'^(\d+)/$', boards_view.boards_topics, name="boards_topics")
    re_path(r'(?P<pk>\d+)/$', boards_view.boards_topics, name="boards_topics"),      # 传递参数
    # re_path(r'\d+/$', boards_view.boards_topics, name="boards_topics") ,           # 不传递参数

    re_path(r'(?P<pk>\d+)/new/$', boards_view.new_topic, name="new_topic"),
    #re_path(r'/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/$', boards_view.topic_show, name="topic_show"),

]
