from django.conf.urls import patterns, include, url


urlpatterns = patterns('',

    url(r'^$', 'socialweb.views.index'),
    url(r'^registro/$', 'socialweb.views.register'), # ADD NEW PATTERN!
    url(r'^registroBanda/$', 'socialweb.views.registerBand'),
    url(r'^registroEvento/$', 'socialweb.views.registerEvent'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name':'auth/login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^nav/$', 'socialweb.views.navbar'),
	)
