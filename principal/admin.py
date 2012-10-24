from principal.models import Parcial
from principal.models import Estudiante
from principal.models import Profesor
from principal.models import Profesor_Materia
from principal.models import Programa
from principal.models import Materia
from django.contrib import admin

admin.site.register(Materia)
admin.site.register(Estudiante)
admin.site.register(Profesor)
admin.site.register(Profesor_Materia)
admin.site.register(Programa)
admin.site.register(Parcial)