#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User
#-----------------------modelos--------------------------------------------------------------
class Materia(models.Model):
	ID_materia = models.BigIntegerField(max_length=50,unique=True,primary_key = True)
	nombre = models.TextField()
	ID_programa = models.BigIntegerField()

	def __unicode__(self):
		return self.nombre

class Parciale(models.Model):
	ID_parcial = models.BigIntegerField(max_length=50,unique=True,primary_key = True)
	ID_materia = models.BigIntegerField()
	ID_profesor = models.BigIntegerField()
	dificultad = models.BigIntegerField()
	nivel = models.BigIntegerField()
	nota =  models.BigIntegerField()
	fecha = models.DateTimeField(auto_now=False)
	semestre = models.BigIntegerField()

	def __unicode__(self):
		return self.nivel	

class Phoja(models.Model):
	ID_parcial = models.BigIntegerField(max_length=50,)
	ID_hoja = models.BigIntegerField(max_length=50,unique=True,primary_key = True)
	numero = models.TextField()
	hoja = models.ImageField(upload_to='parciles', verbose_name='Imágen')	

	def __unicode__(self):
		return self.nivel	


class Carrera(models.Model):
	ID_programa = models.BigIntegerField(max_length=50,unique=True,primary_key = True)
	nombre = models.TextField()
	codigo = models.TextField(unique=True)
	semaforo = models.ImageField(upload_to='semaforos', verbose_name='Imágen')

	def __unicode__(self):
		return self.nombre

class Profesor(models.Model):
	ID_profesor = models.BigIntegerField(max_length=50,unique=True,primary_key = True)
	nombre = models.TextField()
	apellido = models.TextField()
	nick = models.TextField()
	ID_programa= models.BigIntegerField()
	correo1 = models.TextField()
	correo2 = models.TextField()

	def __unicode__(self):
		return self.nivel	

class Cliente(models.Model):
	ID_estudiante = models.BigIntegerField(max_length=50,unique=True,primary_key = True)
	nombre = models.TextField()
	fechanacimiento = models.DateTimeField(auto_now=False)
	apellido = models.TextField()
	ID_programa = models.BigIntegerField()
	correo = models.TextField()
	clave = models.TextField()
	telefono = models.TextField()
    
	def __unicode__(self):
		return self.nivel	

class Profesor_Materia(models.Model):
	ID_profesor = models.BigIntegerField()
	ID_materia = models.BigIntegerField()
	
	def __unicode__(self):
		return self.nivel	

