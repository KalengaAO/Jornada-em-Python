from django.contrib import admin
from .models import Produto

@admin.register(Produto)
class	Produto_admin(admin.ModelAdmin):
	list_display = ("nome", "preco")
	search_field = ("nome", "preco")
