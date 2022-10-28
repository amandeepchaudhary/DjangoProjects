from django.urls import path
from enroll import views


urlpatterns = [
    path('<int:my_id>/', views.details, name="details"),
    path('<int:my_id>/<int:my_subid>/', views.subdetails, name="subdetails"),
]
