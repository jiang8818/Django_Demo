from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hr_home(request):
    return HttpResponse("人生苦短，我用Python")