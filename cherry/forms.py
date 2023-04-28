from django import forms
from cherry.models import *
class TopicForm(forms.Form):
    topic_name=forms.CharField(max_length=100)


class WebpageForm(forms.Form):
    topic_name=forms.CharField(max_length=100)
    name=forms.CharField(max_length=100)
    email=forms.EmailField()





class AccessRecordForm(forms.Form):
    name=forms.CharField(max_length=100)
    author=forms.CharField()
    date=forms.DateField()