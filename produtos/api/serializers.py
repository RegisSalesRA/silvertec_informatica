from produtos.models import Processador
from rest_framework import serializers


class ProcessadorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Processador
        fields = ['marca']
