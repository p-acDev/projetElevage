from rest_framework.serializers import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from mesure.models import MesureAnimal

class MesureAnimalSerializer(ModelSerializer):
    
    animal_name = SerializerMethodField()
    animal_type = SerializerMethodField()
    mesure_type = SerializerMethodField()
    
    def get_animal_name(self, obj):
        return obj.animal.animal_name
    
    def get_animal_type(self, obj):
        return obj.animal.animal_type.type_name
    
    def get_mesure_type(self, obj):
        return obj.mesure_type.type_name
    
    class Meta:
        model = MesureAnimal
        fields = ['animal_name', 'animal_type', 'mesure_type',
                  'mesure_val', 'mesure_date']
