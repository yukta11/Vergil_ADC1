from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

#from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = "vacancy"

urlpatterns = [
    path('vacancyform/', views.vacancyform, name='vacancyform'),
    path('home/', views.home, name='home'),
    path('main/', views.main, name='main'),
    path('book/', views.book, name='book'),
    path('home/<int:pk>', views.deleteprofessor, name='deleteprofessor'),
    path('updateprofile/<int:id>', views.updateprofile, name='updateprofile'),
]
