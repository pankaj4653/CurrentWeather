
from django.urls import path
from . import views

urlpatterns = [
    path('forecast', views.index),
    path('home', views.home),
]