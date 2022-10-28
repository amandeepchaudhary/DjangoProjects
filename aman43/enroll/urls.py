from django.urls import path, register_converter
from enroll import views, converters

register_converter(converters.FourDigitYearConverter, 'yyyy')

urlpatterns = [
    path('session/<int:my_id>/<yyyy:year>/', views.showsessiony, name="year"),  # Where year is the name that can be anything as we like and yyyy is the converter that we want to show
    path('<int:my_id>/', views.details, name="details"),
    path('<int:my_id>/<int:my_subid>/', views.subdetails, name="subdetails"),
]
