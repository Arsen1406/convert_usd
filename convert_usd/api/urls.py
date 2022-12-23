from django.urls import path
from .views import convert_currency

urlpatterns = [
    path('rates/', convert_currency),
]
