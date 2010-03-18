from django.conf.urls.defaults import *
from djangotest.simple.views import main, logoutUser

urlpatterns = patterns('',
    (r'^$', main),
    (r'^logout/$',logoutUser)

)