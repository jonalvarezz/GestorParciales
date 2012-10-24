from django.db import models
#-----------------------modelos--------------------------------------------------------------
class Materia(models.Model):
	ID_materia = models.BigIntegerField(max_length=50,unique=True,primary_key = True)
	nombre= models.TextField()
	codigo = models.TextField(unique=True)
	Programa = models.TextField()

	def __unicode__(self):
		return self.nombre

class Parcial(models.Model):
	ID_parcial = models.BigIntegerField(max_length=50,unique=True,primary_key = True)
	materia= models.TextField()
	profesor = models.TextField()
	dificultad = models.BigIntegerField()
	nivel= models.BigIntegerField()
	fecha= models.DateTimeField(auto_now=False)

	def __unicode__(self):
		return self.nivel	

class Programa(models.Model):
	ID_programa = models.BigIntegerField(max_length=50,unique=True,primary_key = True)
	nombre= models.TextField()
	codigo = models.TextField(unique=True)
	Semaforo = models.ImageField(upload_to='semaforos', verbose_name='Imágen')

	def __unicode__(self):
		return self.nombre

class Profesor(models.Model):
	ID_profesor = models.BigIntegerField(max_length=50,unique=True,primary_key = True)
	nombre= models.TextField()
	apellido= models.TextField()
	nick = models.TextField()
	falcultad= models.TextField()
	correo1= models.TextField()
	correo2= models.TextField()

	def __unicode__(self):
		return self.nivel	

class Estudiante(models.Model):
	ID_estudiante = models.BigIntegerField(max_length=50,unique=True,primary_key = True)
	nombre= models.TextField()
	Apellido = models.TextField()
	correo = models.TextField()
	clave= models.TextField()
	fechanacimiento= models.DateTimeField(auto_now=False)
    carrera= models.TextField()
	telefono= models.TextField()

	def __unicode__(self):
		return self.nivel	

class Profesor_Materia(models.Model):
	ID_profesor = models.BigIntegerField(max_length=50,unique=True,primary_key = True)
	ID_materia= models.BigIntegerField()
	Grupo = models.BigIntegerField()
	Horario = models.TextField()
	Año = models.BigIntegerField()
	
	def __unicode__(self):
		return self.nivel	

