
from django.urls import path
from . import views
from vacancy import urls

app_name = "Authorization"

urlpatterns = [
	path('', views.authentic, name='authentic'),
    path('login/', views.loginForm, name='loginForm'),
    path('register/', views.registerForm, name='registerForm'),
    path('logout/', views.logoutuser, name='logout'),
]