from django.urls import path
from . import views

app_name = "tema"

urlpatterns = [
	path("", views.index, name="index"),
]
