from django.urls import path
from .views import calculate_distance_view

app_name = 'measurements'

urlspatterns = [
    path('', calculate_distance_view, name='calculate-view')
]