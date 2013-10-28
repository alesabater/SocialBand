from pruebaWeb.models import MusicLover, Banda, Evento
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms


class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField(label='Email')

    class Meta:
        model = User
        fields = ('username','email','first_name','last_name')

class UserAlternativeForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField(label='Email')

    class Meta:
        model = User
        exclude= ('first_name','last_name')


    class Meta:
        model = User
        fields = ('username',)
	

class MusicLoverForm(ModelForm):
    us_fecha_nacimiento = forms.DateField(label='fecha de nacimiento')
    class Meta:
	    model = MusicLover
	    fields = ('ml_genero',)

class BandaForm(ModelForm):
    ba_nombre = forms.CharField(label='Nombre')
    ba_integranges = forms.IntegerField(label='# de Integrantes')
    ba_genero = forms.MultipleChoiceField(label='Generos')
    class Meta:
        model = Banda
        fields = ('ba_integranges','ba_nombre','ba_genero')



class EventoForm(ModelForm):
    ev_nombre = forms.CharField(label='Nombre del evento')
    ev_lugar = forms.CharField(label='Lugar')
    ev_fecha = forms.DateField(label='Fecha del evento')
    ev_banda = forms.MultipleChoiceField(label='Bandas asistentes')
    class Meta:
        model = Evento
        fields = ('ev_nombre','ev_banda','ev_fecha','ev_lugar')

