from django.contrib import admin
from .models import Produto, Contacto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
	list_display = ("id", "nome", "preco")

@admin.register(Contacto)
class ContactosAdmin(admin.ModelAdmin):
	list_display = ("id", "nome", "morada", "tel")
