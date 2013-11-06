from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from socialweb.models import *
from forms import *
from django.core.exceptions import ObjectDoesNotExist


@login_required
def navbar(request):
	ba = None;
	ml = None;
	ev = None;
	try:
		ba = Banda.objects.get(ba_user_id = request.user)
	except ObjectDoesNotExist:
		pass
	try:
		ml = MusicLover.objects.get(us_user_id = request.user)
	except ObjectDoesNotExist:
		pass
	try:
		ev = Evento.objects.get(ev_user_id = request.user)
	except ObjectDoesNotExist:
		pass

	
	if ml is not None:
		return render(request, 'usuario.html',{'user':request.user, 'musiclover':ml})
	elif ba is not None:
		return render(request, 'banda.html',{'user':request.user, 'banda':ba})
	else:
		return render(request, 'evento.html',{'user':request.user, 'evento':ev})




def upload_pic(request):

	if request.method == 'POST':

		form = UsuarioPicture(request.POST, request.FILES)
		if form.is_valid():
			m = MusicLover.objects.get(us_user_id=request.user)
        	m.us_picture = request.FILES['us_picture']
        	m.save()
        	return HttpResponseRedirect('/usuario/')
	else:
		form = UsuarioPicture()

	return HttpResponseRedirect('/')

def upload_pic_b(request):

	if request.method == 'POST':

		form = BandaPicture(request.POST, request.FILES)
		if form.is_valid():
			m = Banda.objects.get(ba_user_id=request.user)
        	m.ba_picture = request.FILES['ba_picture']
        	m.save()
        	return HttpResponseRedirect('/usuario/banda/')
	else:
		form = BandaPicture()

	return render(request , 'banda.html', {'form': form})

def upload_pic_e(request):

	if request.method == 'POST':

		form = EventoPicture(request.POST, request.FILES)
		if form.is_valid():
			m = Evento.objects.get(ev_user_id=request.user)
        	m.ev_picture = request.FILES['ev_picture']
        	m.save()
        	return HttpResponseRedirect('/usuario/evento/')
	else:
		form = EventoPicture()

	return HttpResponseRedirect('/usuario/evento/')

def usuario(request):
	ml = MusicLover.objects.get(us_user_id = request.user)
	return render(request, 'usuario.html',{'user':request.user, 'musiclover':ml})

def buscar_eventos(request):
	if request.method == 'POST':
		search_text = request.POST['search_text']
	else:
		search_text = ''
	eventos = Evento.objects.filter(ev_nombre__contains=search_text)

	return render(request, 'prueba.html',{'eventos':eventos})

def buscar_usuarios(request):
	if request.method == 'POST':
		search_text = request.POST['search_text']
	else:
		search_text = ''
	usuarios = User.objects.filter(username__contains=search_text)

	return render(request, 'usuariobusqueda.html',{'usuarios':usuarios})

def evento(request):

	language = 'en-gb'
	session_language = 'en-gb'
    
	if 'lang' in request.COOKIES:
		language = request.COOKIES['lang']
        
	if 'lang' in request.session:
		session_language = request.session['lang']

	args = {}
	args.update(csrf(request))
    
	args['evento'] = Evento.objects.all()
	args['user'] = request.user
	args['language'] = language   
	args['session_language'] = session_language 

    
	return render(request, 'evento.html', args) 

def usuariobusqueda(request):

	language = 'en-gb'
	session_language = 'en-gb'
    
	if 'lang' in request.COOKIES:
		language = request.COOKIES['lang']
        
	if 'lang' in request.session:
		session_language = request.session['lang']

	args = {}
	args.update(csrf(request))
    
	args['usuario'] = User.objects.all()
	args['user'] = request.user
	args['language'] = language   
	args['session_language'] = session_language 

    
	return render(request, 'usuario.html', args) 

def usuariobusqueda(request, username=''):   
    #return render_to_response('article.html', 
                              #{'article': Article.objects.get(id=article_id) },
                              #context_instance=RequestContext(request))

	ba = None;
	ml = None;
	ev = None;
	try:
		ba = Banda.objects.get(ba_user_id = User.objects.get(username=username))
	except ObjectDoesNotExist:
		pass
	try:
		ml = MusicLover.objects.get(us_user_id = User.objects.get(username=username))
	except ObjectDoesNotExist:
		pass
	try:
		ev = Evento.objects.get(ev_user_id = User.objects.get(username=username))
	except ObjectDoesNotExist:
		pass

	
	if ml is not None:
		return render(request, 'usuario.html',{'user':request.user, 'musiclover':ml})
	elif ba is not None:
		return render(request, 'banda.html',{'user':request.user, 'banda':ba})
	else:
		return render(request, 'evento.html',{'user':request.user, 'evento':ev})







def evento(request, ev_nombre=''):   
    #return render_to_response('article.html', 
                              #{'article': Article.objects.get(id=article_id) },
                              #context_instance=RequestContext(request))
	return render(request, 'evento.html', {'evento': Evento.objects.get(ev_nombre=ev_nombre)})

def banda(request):

	language = 'en-gb'
	session_language = 'en-gb'
    
	if 'lang' in request.COOKIES:
		language = request.COOKIES['lang']
        
	if 'lang' in request.session:
		session_language = request.session['lang']

	args = {}
	args.update(csrf(request))
    
	args['banda'] = Banda.objects.all()
	args['user'] = request.user
	args['language'] = language   
	args['session_language'] = session_language 

    
	return render(request, 'banda.html', args) 

def banda(request, ba_nombre=''):   
    #return render_to_response('article.html', 
                              #{'article': Article.objects.get(id=article_id) },
                              #context_instance=RequestContext(request))
	return render(request, 'banda.html', {'banda': Banda.objects.get(ba_nombre=ba_nombre)})

def buscar_bandas(request):
	if request.method == 'POST':
		search_text = request.POST['search_text']
	else:
		search_text = ''
	bandas = Banda.objects.filter(ba_nombre__contains=search_text)

	return render(request, 'bandasearch.html',{'bandas':bandas})

def usuarioprincipal(request):
	ml = None;
	try:
		ml = MusicLover.objects.get(us_user_id = request.user)
	except ObjectDoesNotExist:
		pass
	if ml is not None:
		return render(request, 'usuario.html',{'user':request.user, 'musiclover':ml})
	else:
		return HttpResponseRedirect('/usuario/')

def eventoprincipal(request):
	ev = None;
	try:
		ev = Evento.objects.get(ev_user_id = request.user)
	except ObjectDoesNotExist:
		pass
	if ev is not None:
		return render(request, 'evento.html',{'user':request.user, 'evento':ev})
	else:
		return HttpResponseRedirect('/usuario/')

def bandaprincipal(request):
	ba = None;
	try:
		ba = Banda.objects.get(ba_user_id = request.user)
	except ObjectDoesNotExist:
		pass
	if ba is not None:
		return render(request, 'banda.html',{'user':request.user, 'banda':ba})
	else:
		return HttpResponseRedirect('/usuario/')

"""
@login_required
def navbar(request):
	ba = None;
	ml = None;
	try:
		ba = Banda.objects.get(ba_user_id = request.user)
		ml = MusicLover.objects.get(us_user_id = request.user)
		ev = Evento.objects.get(ev_user_id = request.user)
	except ObjectDoesNotExist:
		pass
	
	if ba is not None:
		return HttpResponseRedirect('usuario/banda/')
	elif ml is not None:
		return HttpResponseRedirect('usuario/usuario',{'musiclover':ml})

	return render(request, 'auth/invalid.html')"""

