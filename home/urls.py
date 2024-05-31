from django.urls import path, include
from .views import HomeView, calculate
urlpatterns = [
    path('', HomeView),
    path('calculate/', calculate, name='calculate'),
]