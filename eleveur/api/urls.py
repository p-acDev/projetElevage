from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MesureAnimalViewSet

route = DefaultRouter()

route.register('mesure-animal', MesureAnimalViewSet)

urlpatterns = [
    path('', include(route.urls)),
]
