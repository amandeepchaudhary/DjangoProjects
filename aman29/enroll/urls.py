from django.urls import path
from enroll import views


urlpatterns = [
    path('Registration/', views.studetails),
    path('thankyou/', views.thankyou),
]