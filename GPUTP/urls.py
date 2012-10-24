from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$','principal.views.inicio'),
#	url(r'^lista/$','principal.views.lista'),
#	url(r'^perfil/$','principal.views.perfil'),
#	url(r'^formularioparcial/$','principal.views.formularioparcial'),
#	url(r'^infoparcial/$','principal.views.infoparcial'),
#	url(r'^infoprofesor/$','principal.views.infoprofesor'),
#	url(r'^infonosotros/$','principal.views.infoprofesor'),		    
#	url(r'^registrar/$','principal.views.infoprofesor'),
#	url(r'^adminprefil/$','principal.views.infoprofesor'),
#	url(r'^quejas/$','principal.views.infoprofesor'),			    
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)