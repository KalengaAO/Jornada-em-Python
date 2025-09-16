from django.urls.conf import include
from django.contrib import admin
from django.urls import path

urlpatterns = [
	path("", include("tema.urls", namespace="tema")),
    path('admin/', admin.site.urls),
]
