from django.urls import path
from django.contrib.auth import views as Views
from . import views

app_name = "user"

urlpatterns = [
	path("login/", Views.LoginView.as_view(template_name='user/login.html'), name='login'),
]
