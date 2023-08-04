from django.contrib import admin
from .models import MesureAnimal, MesureType

# Register your models here.
admin.site.register((MesureAnimal, MesureType))
