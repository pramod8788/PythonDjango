from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name="list"),
	path('login', views.loginPage, name="login-page"),
]
