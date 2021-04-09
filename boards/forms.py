# *_* coding: utf-8 *_*
# time:2021-04-0615:22
# tools:PyCharm
# file_name：forms.py

# 停下休息的时候不要忘记别人还在奔跑！！！
#
#
from django import forms
from .models import Topic


class NewTopicForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(
                              attrs={'row':5,'placeholder':'What is on your mind?'}
                              ),
                              max_length=4000,
                              help_text='The max length of the text is 40000.'
                              )

    class Meta:
        model=Topic
        fields = ['subject', 'message']
