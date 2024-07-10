from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from cars.views import *

urlpatterns = [
    path('cars/', CarAPIList.as_view()),
    path('cars/<int:pk>/', CarAPIUpdate.as_view()),
    path('carsdetails/<int:pk>/', CarAPIDestroy.as_view())
]