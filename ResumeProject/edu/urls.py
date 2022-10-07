from django.urls import path
from edu import views

urlpatterns = [
    path('serv/', views.services,name='services'),
    path('skill/', views.skill,name='skill'),
]