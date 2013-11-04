from django.conf.urls import patterns, include, url


urlpatterns = patterns('',

    url(r'^$', 'socialweb.views.navbar'),
    #url(r'^banda/$', 'socialweb.views.banda'),
	)
