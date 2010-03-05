from django.db import models
from django.forms import ModelForm
from django.forms.extras.widgets import SelectDateWidget
from django import forms
from django.contrib.admin.models import LogEntry
from django.db.models.signals import post_delete, post_save
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User


class UserInfo(models.Model):
    name = models.CharField(max_length=150)
    surname = models.CharField(max_length=150)
    birthday = models.DateField()
    about = models.TextField(max_length=150)
    contacts = models.TextField(max_length=150)
    
    def __unicode__(self):
        return self.name + " " + self.surname

class Counter(models.Model):
    url = models.CharField(max_length=256)
    datetime = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.url

class UserInfoForm(ModelForm):
    birthday = forms.DateField(widget=SelectDateWidget())
    class Meta:
        model = UserInfo


ADD = 1
MODIFY = 2
DELETE = 3

def modifyaddsignal(sender, **kwargs):
    if issubclass(sender, UserInfo) or issubclass(sender, Counter):
        #couse fixtures initial problem
        try:
            instance = kwargs['instance']
            created = kwargs['created']
            object_id = instance.id
            object_repr = instance.__unicode__()
            if created:
                action_flag = ADD
            else:
                action_flag = MODIFY
            content_type = ContentType.objects.get(name="log entry")
            user = User.objects.all()[0]
            log_entry = LogEntry(object_id=object_id, object_repr = object_repr, action_flag = action_flag, content_type = content_type, user = user)
            log_entry.save()
        except:
            pass

post_save.connect(modifyaddsignal)

def deletesignal(sender, **kwargs):
    if issubclass(sender, UserInfo) or issubclass(sender, Counter):
        #couse fixtures initial problem
        try:
            instance = kwargs['instance']
            object_id = instance.id
            object_repr = instance.__unicode__()
            action_flag = DELETE
            content_type = ContentType.objects.get(name="log entry")
            user = User.objects.all()[0]
            log_entry = LogEntry(object_id=object_id, object_repr = object_repr, action_flag = action_flag, content_type = content_type, user = user)
            log_entry.save()
        except:
            pass


post_delete.connect(deletesignal)
