from django.conf.urls.defaults import *
from djangotest.simple.views import main, edit, logout_user

urlpatterns = patterns('',
    (r'^$', main),
    (r'^edit/$', edit),
    (r'^logout/$',logout_user)
)
