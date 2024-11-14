from rest_framework.serializers import ModelSerializer
from .models import Category,Kurs,Malim


class Categoryserializers(ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'



class KursSerializers(ModelSerializer):
    class Meta:
        model=Kurs
        fields='__all__'




class MalimSerializers(ModelSerializer):
    class Meta:
        model=Malim
        fields='__all__'






