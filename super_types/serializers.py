from rest_framework import serializers
from .models import Super_Types


class Super_Types_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Super_Types
        fields = ['hero', 'villain']
    
        