# Nikhita Guntu gjs2xs
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('main/go-map/', views.goToMap, name='add-item'),

]