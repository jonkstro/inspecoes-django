from rest_framework import serializers
from plataforma.models import PlanoManut

class PlanoManutSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanoManut
        fields = '__all__'