from django.shortcuts import render, get_object_or_404 , redirect
from django.http import HttpResponse
from .models import Produto, Contacto
from .forms import ProdutoForm

def index(request):
	lista_produto = []
	lista_contacto = []
	produto = Produto.objects.all()
	contact = Contacto.objects.all()
	return render(request,"polls/index.html", {"produto": produto, "contacto": contact})

def adicionar_produto(request):
	if request.method == "POST":
		form = ProdutoForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("polls:index")
	else:
		form = ProdutoForm()
	return render(request, "polls/novo_produto.html", { "form":form })

def detail(request, pk):
	produto = get_object_or_404(Produto, pk=pk)
	return render(request, "polls/detail.html", {"produto": produto})
