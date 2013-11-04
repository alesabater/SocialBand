from django import forms
from models import MusicLover
from django.forms import ModelForm


class UsuarioPicture(ModelForm):

    class Meta:
    	model = MusicLover
    	fields = ('us_picture',)






 