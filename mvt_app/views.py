from django.shortcuts import render
from django.http import HttpResponse
from mvt_app.models import Familiares


# Create your views here.
def inicio(request):

    dict_ctx = {"title": "Inicio", "message": "Bienvenid@"}
    return render(request, "mvt_app/base.html", dict_ctx)

def listar(request):  

    fichas = Familiares.objects.all()  

    return render(request, "mvt_app/listar_fichas.html", {"fichas": fichas})