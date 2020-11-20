from montagem.models import Montagem
from rest_framework import serializers


class MontagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Montagem
        fields = ['nome', 'processador', 'placamae', 'memoria', 'placadevideo']
