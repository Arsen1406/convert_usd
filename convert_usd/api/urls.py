from django.urls import include, path
from rest_framework import routers
from .views import convert_valute

router = routers.DefaultRouter()
params = {'key1': 'value1', 'key2': 'value2', 'key3': 'count'}
urlpatterns = [
    path('', include(router.urls)),
    path(r'rates/params/', convert_valute),
]