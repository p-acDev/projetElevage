from django.db import models
from animal.models import FarmAnimal

# Create your models here.
class MesureType(models.Model):
    type_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.type_name

class MesureAnimal(models.Model):
    animal = models.ForeignKey(FarmAnimal, on_delete=models.CASCADE)
    mesure_type = models.ForeignKey(MesureType, on_delete=models.CASCADE)
    mesure_val = models.FloatField()
    mesure_date = models.DateField()
    
    def __str__(self):
        return f"{self.animal} - {self.mesure_type} - {self.mesure_val} - {self.mesure_date}"