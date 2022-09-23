from django.urls import path
from course import views

urlpatterns = [
    path('learndj/', views.learn_Django),
    path('learnpy/', views.learn_Python)
]