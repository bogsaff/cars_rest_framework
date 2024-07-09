from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from cars import views

urlpatterns = [
    path('cars/', views.Cars.as_view()),
]