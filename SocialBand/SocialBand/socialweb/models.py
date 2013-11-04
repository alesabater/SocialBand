from django.db import models
from django.contrib.auth.models import User



class Genero(models.Model):

	gen_nombre = models.CharField(max_length=50)
	gen_id = models.AutoField(primary_key=True)

	def __unicode__(self):
		return self.gen_nombre

class Banda(models.Model):
	ba_user_id = models.OneToOneField(User, db_column='id', primary_key=True)
	ba_nombre = models.CharField(max_length=200)
	ba_picture = models.ImageField(upload_to = 'media/', default = 'nopic.jpg')
	ba_genero = models.ManyToManyField(Genero, blank=True)
	ba_integrantes = models.IntegerField()

class Evento(models.Model):
	ev_user_id = models.OneToOneField(User, db_column='id', primary_key=True)
	ev_nombre = models.CharField(max_length=200)
	ev_picture = models.ImageField(upload_to = '/media/', default = 'nopic.jpg')
	ev_lugar = models.CharField(max_length=1000)
	ev_fecha = models.DateField()
	ev_banda = models.ManyToManyField(Banda, blank=True)

	@classmethod
	def create(cls, ev_user_id, ev_lugar, ev_fecha, ev_nombre):
		evento = cls(us_user_id=us_user_id, ev_lugar=ev_lugar, ev_fecha=ev_fecha, ev_nombre=ev_nombre)
		return evento

class MusicLover(models.Model):
	us_fecha_nacimiento = models.DateField(null=True, blank=True)
	us_picture = models.ImageField(upload_to = 'media/', default = 'nopic.jpg')
	us_user_id = models.OneToOneField(User, db_column='id', primary_key=True)
	ml_genero = models.ManyToManyField(Genero, blank=True)
	ml_banda = models.ManyToManyField(Banda, blank=True)
	ml_evento = models.ManyToManyField(Evento, blank=True)

	@classmethod
	def create(cls, us_user_id):
		musiclover = cls(us_user_id=us_user_id)
		return musiclover




# Create your models here.
