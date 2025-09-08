from django.shortcuts import render
from django.http import HttpResponse
from .models import Produto, Contacto

def index(request):
	lista_produto = []
	lista_contacto = []
	produto = Produto.objects.all()
	contact = Contacto.objects.all()
	return render(request,"polls/index.html", {"produto": produto, "contacto": contact})

def produto_detail(request, pk):
	produto = get_object_or_404(Produto, pk=pk)
	return render(request, "polls/detail.html", {"produto": produto})
