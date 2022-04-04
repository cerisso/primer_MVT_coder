from django.urls import path
from mvt_app.views import *

urlpatterns = [
    
    path("", inicio, name = "inicio" ),

    path("listar/",listar, name = "listar"),



]
