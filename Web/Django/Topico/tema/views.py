from django.shortcuts import render, redirect, get_object_or_404
from .models import Tema, Subtema
from .forms import FormTopico, FormSubtema, EditarForm

def index(request):
	return render(request, "tema/index.html")

def tema(request):
	topicos = Subtema.objects.all()
	return render(request, "tema/topico.html", {"topicos": topicos})

def form(request):
	if request.method == "POST":
		form = FormTopico(request.POST)	
		if form.is_valid():
			form.save()
		return redirect("tema:index")
	form = FormTopico()
	return render(request, "tema/new_topico.html", {"form": form})

def	lista(request):
	lista = Tema.objects.all()
	return render(request, "tema/lista_topico.html", {"lista": lista})

def subtema(request, pk):
	tema = get_object_or_404(Tema, id=pk)
	if request.method == "POST":
		form = FormSubtema(request.POST)
		if form.is_valid():
			new_subtema = form.save(commit=False)
			new_subtema.topico = tema
			new_subtema.save()
		return redirect("tema:index")
	form = FormSubtema()
	return render(request, "tema/new_subtema.html", {"tema": tema, "form": form})

def	editarsub(request, pk):
	sub = get_object_or_404(Subtema, id=pk)
	campo = sub.topico
	if request.method == "POST":
		form = EditarForm(instance=sub, data=request.POST)
		if form.is_valid():
			form.save()
			return redirect("tema:topico")
	form = EditarForm(instance=sub)
	return render(request, "tema/editarsub.html", {"sub": sub, "campo": campo, "form": form})
