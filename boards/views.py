from django.shortcuts import render
from django.http import HttpResponse
from boards.models import Board, Topic, Post


# Create your views here.
def boards_home(request):
    boards = Board.objects.all()
    return render(request, 'board_home.html', {'boards': boards})
