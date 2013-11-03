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
	#ba_picture = models.ImageField(upload_to = '/media/', default = 'nopic.jpg')
	ba_genero = models.ManyToManyField(Genero)
	ba_integrantes = models.IntegerField()

class Evento(models.Model):
	ev_user_id = models.OneToOneField(User, db_column='id', primary_key=True)
	ev_nombre = models.CharField(max_length=200)
	#ev_picture = models.ImageField(upload_to = '/media/', default = 'nopic.jpg')
	ev_lugar = models.CharField(max_length=1000)
	ev_fecha = models.DateTimeField()
	ev_banda = models.ManyToManyField(Banda)

class MusicLover(models.Model):
	us_fecha_nacimiento = models.DateField(blank=True)
	us_picture = models.ImageField(upload_to = '/media/', default = 'nopic.jpg')
	us_user_id = models.OneToOneField(User, db_column='id', primary_key=True)
	ml_genero = models.ManyToManyField(Genero)
	ml_banda = models.ManyToManyField(Banda, blank=True)
	ml_evento = models.ManyToManyField(Evento, blank=True)





# Create your models here.
