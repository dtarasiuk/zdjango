from django.conf.urls.defaults import *
from djangotest.simple.views import main

urlpatterns = patterns('',
    # Example:
    (r'^$', main),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

)
