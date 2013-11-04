from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from socialweb.models import *
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
	"""else:
		return render(request, 'evento.html',{'user':request.user, 'evento':ev})"""

	

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

	return render(request, 'auth/invalid.html')

def usuario(request):
	
	return render(request, 'navbar.html',{'user':request.user, 'musiclover':ml})"""
