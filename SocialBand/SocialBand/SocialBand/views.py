from django.shortcuts import render, render_to_response
from forms import EventoForm, RegistrationForm, BandaForm
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from socialweb.models import *



def logout_page(request):
    """
    Log users out and re-direct them to the main page.
    """
    logout(request)
    return HttpResponseRedirect('/')

def index(request):
	return render(request, 'index.html',{'user':request.user})

def registration_success(request):
	return render(request, 'auth/registration_success.html')

def registerBanda(request):

	registered = False

	if request.method == 'POST':
		form = RegistrationForm(data=request.POST)
		banda_form = BandaForm(data = request.POST)

		if form.is_valid() and banda_form.is_valid:
			user = User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'], form.cleaned_data['password1'])
			user.save()
			banda = banda_form.save()
			banda.save()
			usuario = auth.authenticate(username=request.POST['username'], password=request.POST['password1'])
			login(request,usuario)
			return HttpResponseRedirect('/')

		else:

			print form.errors, banda_form.errors

	else:

		form = RegistrationForm()
		banda_form = BandaForm()

	return render(request, 'registroBanda1.html', {'user':form, 'banda_form':banda_form, 'registered':registered})

def registerEvent(request):

	registered = False

	if request.method == 'POST':
		form = RegistrationForm(data=request.POST)
		evento_form = EventoForm(data = request.POST)

		if form.is_valid() and evento_form.is_valid:
			user = User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'], form.cleaned_data['password1'])
			user.save()
			evento = evento_form.save()
			evento.save()
			usuario = auth.authenticate(username=request.POST['username'], password=request.POST['password1'])
			login(request,usuario)
			return HttpResponseRedirect('/')

		else:

			print form.errors, evento_form.errors

	else:

		form = RegistrationForm()
		evento_form = EventoForm()

	return render(request, 'registroEvento1.html', {'user':form, 'evento_form':evento_form, 'registered':registered})

def registro1(request):

	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'], form.cleaned_data['password1'])
			user.save()
			musiclover = MusicLover.create(user)
			musiclover.save()
			usuario = auth.authenticate(username=request.POST['username'], password=request.POST['password1'])
			login(request,usuario)
			return HttpResponseRedirect('/')

	args = {}
	args.update(csrf(request))
	args['form']=RegistrationForm()

	return render_to_response('registro1.html',args)