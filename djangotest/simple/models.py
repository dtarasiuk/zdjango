from django.db import models

class UserInfo(models.Model):
    name = models.CharField(max_length=150)
    surname = models.CharField(max_length=150)
    about = models.TextField(max_length=150)
    contacts = models.TextField(max_length=150)
