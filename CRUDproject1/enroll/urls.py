from django.urls import path 
from enroll import views

urlpatterns = [
    path('', views.add_show, name="addshow"),
    path('update/<int:id>/', views.update_edit, name="updatedata"),
    path('delete/<int:id>/', views.delete_stu, name="deletedata"),
]