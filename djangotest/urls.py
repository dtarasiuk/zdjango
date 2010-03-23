from django.conf.urls.defaults import *
from simple.views import main

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', main, name="main_page"),
    (r'^simple/', include('djangotest.simple.urls')),
    (r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^admin/(.*)', admin.site.root),
)
