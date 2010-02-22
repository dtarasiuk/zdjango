from django.db import models
from django.forms import ModelForm


class UserInfo(models.Model):
    name = models.CharField(max_length=150)
    surname = models.CharField(max_length=150)
    about = models.TextField(max_length=150)
    contacts = models.TextField(max_length=150)

class Counter(models.Model):
    url = models.CharField(max_length=256)
    datetime = models.DateTimeField(auto_now=True)

class UserInfoForm(ModelForm):
    class Meta:
        model = UserInfo