from django.conf.urls.defaults import *
from djangotest.simple.views import main, edit, logoutUser

urlpatterns = patterns('',
    (r'^$', main),
    (r'^edit/$', edit),
    (r'^logout/$',logoutUser)

)