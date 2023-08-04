from django.contrib import admin
from .models import AnimalType, FarmAnimal

# Register your models here.
admin.site.register((AnimalType, FarmAnimal))
