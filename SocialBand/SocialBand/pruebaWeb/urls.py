from django.conf.urls import patterns, include, url


urlpatterns = patterns('',

    url(r'^$', 'pruebaWeb.views.index'),
    url(r'^registro/$', 'pruebaWeb.views.register'), # ADD NEW PATTERN!
    url(r'^registroBanda/$', 'pruebaWeb.views.registerBand'),
    url(r'^registroEvento/$', 'pruebaWeb.views.registerEvent'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name':'auth/login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
	)
