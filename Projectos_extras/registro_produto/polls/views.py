from django.shortcuts import render
from .models import Produto

def index(request):
	produto = Produto.objects.all():
	return render(request, "polls/index.html", {"produto": produto})
