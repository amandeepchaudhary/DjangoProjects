from django.urls import path
from todays import views

urlpatterns = [
    path('', views.todays),
]