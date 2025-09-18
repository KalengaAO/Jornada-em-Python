from django.urls import path
from .views import 


urlpatterns = [
	path("login/", views.login, name="login"),
	path("logout/", views.logout, name="logout"),
]
