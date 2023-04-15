# Nikhita Guntu gjs2xs

from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='index'),
    path('main/go-map/', views.goToMap, name='add-item'),

]
