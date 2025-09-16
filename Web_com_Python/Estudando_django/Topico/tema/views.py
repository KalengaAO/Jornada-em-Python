from django.shortcuts import render
from .models import Tema, Subtema

def index(request):
	return render(request, "tema/index.html")

def tema(request):
	topicos = Subtema.objects.all()
	return render(request, "tema/topico.html", {"topicos": topicos})
