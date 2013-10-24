"""from django.db import models
from django.contrib.auth.models import User


class Usuario(models.Model):

	us_email = models.EmailField(unique=True)
	us_auth_user = models.OneToOneField(User)
	us_id = models.AutoField(primary_key=True)

class MusicLover(models.Model):
	us_fecha_nacimiento = models.DateField()
	us_first_name = models.CharField(max_lenght=200)
	us_last_name = models.CharField(max_lenght=75)
	ml_us_id = models.OneToOneField(Usuario)
	ml_genero = models.ManyToManyField(Genero)
	ml_id = models.AutoField(primary_key=True)
	ml_banda = models.ManyToManyField(Banda)
	ml_evento = models.ManyToManyField(Evento)


class Genero(models.Model):
	gen_nombre = models.CharField(max_lenght=50)
	gen_id = models.AutoField(primary_key=True)

class Banda(models.Model):
	ba_us_id = models.ForeignKey(Usuario)
	ba_nombre = models.CharField(max_lenght=200)
	ba_genero = models.ManyToManyField(Genero)
	ba_integrantes = models.IntegerField()
	ba_id = models.AutoField(primary_key=True)

class Evento(models.Model):
	ev_us_id = models.ForeignKey(Usuario)
	ev_nombre = models.CharField(max_lenght=200)
	ev_lugar = models.CharField(max_lenght=1000)
	ev_fecha = models.DateTimeField()
	ev_banda = models.ManyToManyField(Banda)
"""

# Create your models here.
