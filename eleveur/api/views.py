from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import MesureAnimalSerializer
from mesure.models import MesureAnimal

# Create your views here.

class MesureAnimalViewSet(ModelViewSet):
    queryset = MesureAnimal.objects.all()
    serializer_class = MesureAnimalSerializer
