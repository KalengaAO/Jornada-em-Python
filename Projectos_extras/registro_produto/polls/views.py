from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto
from .forms import ProdutoForm

def index(request):
	produto = Produto.objects.all()
	return render(request, "polls/index.html", {"produto": produto})

def detail(request, pk):
	produto = get_object_or_404(Produto, pk=pk)
	return render(request, "polls/detail.html", {"produto": produto})

def adicionar_produto(request):
	if request.method == "POST":
		form = ProdutoForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("polls:index")
	else:
		form = ProdutoForm()
	return render(request, "polls/form_produto.html", {"form": form})
