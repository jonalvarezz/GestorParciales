from principal.models import Parciale
from principal.models import Cliente
from principal.models import Profesor
from principal.models import Profesor_Materia
from principal.models import Carrera
from principal.models import Materia
from principal.models import Phoja
from django.contrib import admin

admin.site.register(Cliente)
admin.site.register(Materia)
admin.site.register(Profesor)
admin.site.register(Profesor_Materia)
admin.site.register(Carrera)
admin.site.register(Parciale)
admin.site.register(Phoja)
