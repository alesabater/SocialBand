from django.conf.urls import patterns, include, url


urlpatterns = patterns('',

    url(r'^$', 'socialweb.views.navbar'),
    url(r'^imagechange/$', 'socialweb.views.upload_pic'),
    url(r'^banda/imagechange/$', 'socialweb.views.upload_pic_b'),
    url(r'^evento/imagechange/$', 'socialweb.views.upload_pic_e'),
    url(r'^usuario/$', 'socialweb.views.usuarioprincipal'),
    url(r'^evento/$', 'socialweb.views.eventoprincipal'),
    url(r'^banda/$', 'socialweb.views.bandaprincipal'),
	url(r'^evento/search/$', 'socialweb.views.buscar_eventos'),
	url(r'^evento/get/(?P<ev_nombre>\w+)/$', 'socialweb.views.evento'),
	url(r'^banda/search/$', 'socialweb.views.buscar_bandas'),
	url(r'^banda/get/(?P<ba_nombre>\w+)/$', 'socialweb.views.banda'),
    url(r'^usuario/search/$', 'socialweb.views.buscar_usuarios'),
    url(r'^usuario/get/(?P<username>\w+)/$', 'socialweb.views.usuariobusqueda'),
    #url(r'^banda/$', 'socialweb.views.banda'),
	)
