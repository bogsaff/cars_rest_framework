from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from cars import views

urlpatterns = format_suffix_patterns([
    path('cars/', views.Cars.as_view(), name='car-list'),
])