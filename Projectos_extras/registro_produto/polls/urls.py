#!/usr/bin/env python3

from django.urls import path
from . import views

app_name = "polls"

urlpatterns = [
	path("", views.index, name="index"),
	path("detail/<int:pk>", views.detail, name="detail"),
	path("novo/", views.adicionar_produto, name="adicionar_produto")
]
