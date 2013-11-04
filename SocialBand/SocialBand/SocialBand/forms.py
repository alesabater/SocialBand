from socialweb.models import MusicLover, Banda, Evento
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    #first_name = forms.CharField(required=True)
    #last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ('username','email','password1','password2')

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        #user.first_name = self.cleaned_data['first_name']
        #user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
        return user

class EventoForm(ModelForm):
    class Meta:
        model=Evento
        fields=('ev_nombre','ev_lugar','ev_fecha')

class BandaForm(ModelForm):
    class Meta:
        model = Banda
        fields = ('ba_nombre','ba_integrantes')


"""class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    #email = forms.EmailField(label='Email')

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
    #us_fecha_nacimiento = forms.DateField(label='fecha de nacimiento')
    #us_picture = forms.ImageField()
    class Meta:
	    model = MusicLover
	    fields = ('ml_genero','us_fecha_nacimiento')

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
        fields = ('ev_nombre','ev_banda','ev_fecha','ev_lugar')"""

