from django.shortcuts import render
from django.http import HttpResponse
from .models import Produto, Contacto

def index(request):
	lista_produto = []
	lista_contacto = []
	produto = Produto.objects.all()
	contact = Contacto.objects.all()
	for p in produto:
		lista_produto.append({"nome": p.nome, "preco": p.preco})
	for c in contact:
		lista_contacto.append({"nome": c.nome, "morada": c.morada, "telefone": c.tel})
	return HttpResponse(f"Produtos disponíveis: {lista_produto}\n {lista_contacto}")
