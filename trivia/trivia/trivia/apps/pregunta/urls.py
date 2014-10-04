from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import *

urlpatterns = patterns('',
    url(r'^$', pagina_index),
	url(r'^esperas/',pagina_juego_espera),
	url(r'^empezados/',pagina_juego_empezado),
)