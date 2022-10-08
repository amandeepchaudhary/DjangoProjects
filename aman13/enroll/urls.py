from django.urls import path
from enroll import views

urlpatterns = [
    path('1/', views.students),
]