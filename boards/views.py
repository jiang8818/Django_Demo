from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from boards.models import Board, Topic, Post
from django.contrib.auth.models import User
from .forms import NewTopicForm


# Create your views here.
def boards_home(request):
    boards = Board.objects.all()
    return render(request, 'board_home.html', {'boards': boards})


# def boards_topics(request,pk):
#     try:
#         boards=Board.objects.get(pk=pk)
#     except Board.DoesNotExist:
#         raise Http404
#     return render(request,'topics.html',{'boards':boards})
#     # return HttpResponse("this is a test")


def boards_topics(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'topics.html', {'board': board})
    # return HttpResponse("this is a test")


#
# def new_topic(request, pk):
#     board = get_object_or_404(Board, pk=pk)
#     if request.method=='POST':
#         subject=request.POST['subject']
#         message=request.POST['message']
#         user = User.objects.first()
#
#         topic = Topic.objects.create(
#             subject=subject,
#             board=board,
#             starter=user
#         )
#         post = Post.objects.create(
#             message=message,
#             topic=topic,
#             created_by=user
#         )
#         return redirect('boards_topics', pk=board.pk)
#     return render(request, 'new_topic.html', {'board': board})


def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    user = User.objects.first()
    if request.method == "POST":
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = user
            topic.save()
            post = Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=user
            )
            return redirect('boards_topics', pk=board.pk)
    else:
        form = NewTopicForm()
    return render(request, 'new_topic.html', {'board': board, 'form': form})
