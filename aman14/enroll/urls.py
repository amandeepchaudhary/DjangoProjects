from django.urls import path
from enroll import views

urlpatterns = [
    path('', views.stuhome),
    path('info/', views.stuinfo,name='info')
]