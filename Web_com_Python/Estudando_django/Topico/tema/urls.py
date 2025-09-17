from django.urls import path
from . import views

app_name = "tema"

urlpatterns = [
	path("", views.index, name="index"),
	path("topico/", views.tema, name="topico"),
	path("new_topico/", views.form, name="form"),
	path("lista/", views.lista, name="lista"),
	path("subtema/<int:pk>", views.subtema, name="subtema"),
	path("editarsub/<int:pk>", views.editarsub, name="editar"),
]
