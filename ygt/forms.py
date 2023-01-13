from django import forms
from.models import Message, Exam, Good
from django.contrib.auth.models import User

# 資格投稿フォーム
class ExamForm(forms.Form):
    title = forms.CharField(label='title')
    cert = forms.CharField(label='cert')
    date = forms.DateField(label='date')
    tool_1 = forms.CharField(label='tool_1')
    tool_2 = forms.CharField(label='tool_2')
    tool_3 = forms.CharField(label='tool_3')
    scd = forms.CharField(max_length=500, \
        widget=forms.Textarea(attrs={'class':'form-control', 'rows':2}))

# メッセージフォーム
class MessageForm(forms.Form):
    content = forms.CharField(max_length=500, \
        widget=forms.Textarea(attrs={'class':'form-control', 'rows':2}))
