# Create your views here.
from principal.models import Parcial
from principal.models import Estudiante
from principal.models import Profesor
from principal.models import Profesor_Materia
from principal.models import Programa
from principal.models import Materia
from principal.models import Parcialhoja
from django.shortcuts import render_to_response

def lista_materias(request):
	materias = Materia.objects.all()
	return render_to_response('lista_materias.html',{'lista':materias})
