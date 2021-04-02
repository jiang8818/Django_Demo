from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hr_home(request):
    return render(request,'hr_home.html')
