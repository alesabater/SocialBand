from django.db import models
from django.contrib.auth.models import User



class Genero(models.Model):

	gen_nombre = models.CharField(max_length=50)
	gen_id = models.AutoField(primary_key=True)

	def __unicode__(self):
		return self.gen_nombre

class Banda(models.Model):
	ba_us_id = models.OneToOneField(User)
	ba_nombre = models.CharField(max_length=200)
	ba_genero = models.ManyToManyField(Genero)
	ba_integrantes = models.IntegerField()
	ba_id = models.AutoField(primary_key=True)

class Evento(models.Model):
	ev_us_id = models.OneToOneField(User)
	ev_nombre = models.CharField(max_length=200)
	ev_lugar = models.CharField(max_length=1000)
	ev_fecha = models.DateTimeField()
	ev_banda = models.ManyToManyField(Banda)

class MusicLover(models.Model):
	us_fecha_nacimiento = models.DateField()
	ml_user = models.OneToOneField(User)
	ml_genero = models.ManyToManyField(Genero)
	ml_id = models.AutoField(primary_key=True)
	#ml_banda = models.ManyToManyField(Banda, blank=True)
	#ml_evento = models.ManyToManyField(Evento, blank=True)





# Create your models here.
