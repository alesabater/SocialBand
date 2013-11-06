from django import forms
from models import *
from django.forms import ModelForm


class UsuarioPicture(ModelForm):

    class Meta:
    	model = MusicLover
    	fields = ('us_picture',)

class BandaPicture(ModelForm):

    class Meta:
    	model = Banda
    	fields = ('ba_picture',)

class EventoPicture(ModelForm):

    class Meta:
    	model = Evento
    	fields = ('ev_picture',)





 