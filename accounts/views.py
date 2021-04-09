from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from .forms import SingUpForm


# Create your views here.
# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             auth_login(request, user)
#             return redirect('boards_home')
#     else:
#         form = UserCreationForm()
#     return render(request, 'sign_up.html', {'form': form})
#     # return HttpResponse("this is a test!")


def signup(request):
    if request.method == 'POST':
        form = SingUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('boards_home')
    else:
        form = SingUpForm()
    return render(request, 'sign_up.html', {'form': form})
