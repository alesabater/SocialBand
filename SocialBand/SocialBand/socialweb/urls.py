from django.conf.urls import patterns, include, url


urlpatterns = patterns('',

    url(r'^$', 'socialweb.views.navbar'),
    url(r'^usuario/imagechange/$', 'socialweb.views.upload_pic'),
    url(r'^usuario/$', 'socialweb.views.usuario'),
    url(r'^evento/$', 'socialweb.views.eventoprincipal'),
    url(r'^banda/$', 'socialweb.views.bandaprincipal'),
	url(r'^usuario/search/$', 'socialweb.views.buscar_eventos'),
	url(r'^usuario/get/(?P<ev_nombre>\w+)/$', 'socialweb.views.evento'),
	url(r'^banda/search/$', 'socialweb.views.buscar_bandas'),
	url(r'^banda/get/(?P<ba_nombre>\w+)/$', 'socialweb.views.banda'),
    #url(r'^banda/$', 'socialweb.views.banda'),
	)
