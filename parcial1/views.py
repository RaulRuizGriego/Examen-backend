from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Pagina de inicio - Examen</h1>")

def about(request):
    return HttpResponse("<h1>Acerca de - Parcial 1</h1>")
# Create your views here.
