from django.conf.urls import *
from views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SocialBand.views.home', name='home'),
    # url(r'^SocialBand/', include('SocialBand.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$', index),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name':'auth/login1.html'}),
    url(r'^logout/$', logout_page),
    url(r'^registro/$', registro1),
    url(r'^registroBanda/$', registerBanda),
    url(r'^registroEvento/$', registerEvent),
    url(r'^usuario/', include('socialweb.urls')),
	)
