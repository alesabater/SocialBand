from django.shortcuts import render, render_to_response
from forms import UserForm, MusicLoverForm, EventoForm, BandaForm, UserAlternativeForm
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from forms import RegistrationForm
from django.contrib.auth.models import User



def logout_page(request):
    """
    Log users out and re-direct them to the main page.
    """
    logout(request)
    return HttpResponseRedirect('/')


def register_user(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'], form.cleaned_data['password1'])
			user.save()
			usuario = auth.authenticate(username=request.POST['username'], password=request.POST['password1'])
			login(request,usuario)
			return HttpResponseRedirect('/')

	args = {}
	args.update(csrf(request))
	args['form']=RegistrationForm()
	return render_to_response('registro.html',args)

def index(request):
	return render(request, 'index.html',{'user':request.user})

def registration_success(request):
	return render(request, 'auth/registration_success.html')

def register(request):
	registered = False

	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		musiclover_form = MusicLoverForm(data = request.POST)

		if user_form.is_valid and musiclover_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()

			musiclover = musiclover_form.save(commit=False)
			musiclover.user= user
			musiclover.save()
			
			#ingreso(request=request)
			#usuario = authenticate(username=request.user.username, password=request.user.pass)
			#login(request, request.usuario)

			registered=True

			return HttpResponseRedirect('/login')
		else:

			print user_form.errors, musiclover_form.errors

	else:

		user_form = UserForm()
		musiclover_form = MusicLoverForm()

	return render(request, 'registro.html', {'user_form':user_form, 'musiclover_form':musiclover_form, 'registered':registered})

def registerBand(request):
	registered = False

	if request.method == 'POST':
		
		user_form = UserAlternativeForm(data=request.POST)
		banda_form = BandaForm(data = request.POST)

		if user_form.is_valid and banda_form.is_valid():
			user = user_form.save(commit=False)
			user.set_password(user.password)
			user.save()

			banda = banda_form.save(commit=False)
			banda.ba_us_id = user
			banda.save()

			registered=True
			return HttpResponseRedirect('/')

		else:

			print user_form.errors, banda_form.errors

	else:

		user_form = UserAlternativeForm()
		banda_form = BandaForm()

	return render(request, 'registroBanda.html', {'user_form':user_form, 'banda_form':banda_form, 'registered':registered})

def registerEvent(request):

	registered = False

	if request.method == 'POST':
		user_form = UserAlternativeForm(data=request.POST)
		evento_form = EventoForm(data = request.POST)

		if user_form.is_valid and evento_form.is_valid():
			user = user_form.save(commit=False)
			user.set_password(user.password)
			user.save()

			evento = evento_form.save(commit=False)
			evento.ev_us_id = user
			evento.save()

			registered=True
			return HttpResponseRedirect('/')

		else:

			print user_form.errors, evento_form.errors

	else:

		user_form = UserAlternativeForm()
		evento_form = EventoForm()

	return render(request, 'registroEvento.html', {'user_form':user_form, 'evento_form':evento_form, 'registered':registered})


