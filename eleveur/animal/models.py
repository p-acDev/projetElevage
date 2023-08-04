from django.db import models

# Create your models here.
class AnimalType(models.Model):
    type_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.type_name

class FarmAnimal(models.Model):
    animal_name = models.CharField(max_length=50, null=True, blank=True)
    animal_type = models.ForeignKey(AnimalType, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.animal_name