from django.urls import path
from . import views
from django.contrib import admin
from . import views
  
urlpatterns = [
	# path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
   
]