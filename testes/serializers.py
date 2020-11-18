from .models import Campos
from rest_framework import serializers


class CampoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campos
        fields = ['nome','idade','quantidade']

        