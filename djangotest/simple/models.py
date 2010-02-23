from django.db import models
from django.forms import ModelForm
from django.forms.extras.widgets import SelectDateWidget
from django import forms


class UserInfo(models.Model):
    name = models.CharField(max_length=150)
    surname = models.CharField(max_length=150)
    birthday = models.DateField()
    about = models.TextField(max_length=150)
    contacts = models.TextField(max_length=150)

class Counter(models.Model):
    url = models.CharField(max_length=256)
    datetime = models.DateTimeField(auto_now=True)

class UserInfoForm(ModelForm):
    birthday = forms.DateField(widget=SelectDateWidget())
    class Meta:
        model = UserInfo