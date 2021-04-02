# *_* coding: utf-8 *_*
# time:2021-04-0214:46
# tools:PyCharm
# file_name：view.py

# 停下休息的时候不要忘记别人还在奔跑！！！
#
#
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse('人生苦短，我用Python!')
    return render(request,'home.html')