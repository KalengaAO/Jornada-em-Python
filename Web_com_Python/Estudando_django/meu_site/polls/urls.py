#!/usr/bin/env python3

from django.urls import path
from . import views

app_name = "polls"

urlpatterns = [
	path("", views.index, name="index"),
	path("produto/<int:pk>/", views.detail, name="detail")
]
