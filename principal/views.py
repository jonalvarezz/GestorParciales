# Create your views here.
from principal.models import Parciale
from principal.models import Cliente
from principal.models import Profesor
from principal.models import Profesor_Materia
from principal.models import Carrera
from principal.models import Materia
from principal.models import Phoja
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404

def lista_materias(request):
	materias = Materia.objects.all()
	return render_to_response('lista_materias.html',{'lista':materias})
