from django.urls import path
from course import views

urlpatterns = [
    path('course/', views.learn_course,name='cor'),
    path('corpy/', views.learn_python,name='corpy'),
    path('cordj/', views.learn_django,name='cordj'),
    path('corjs/', views.learn_javascript,name='corjs'),
]