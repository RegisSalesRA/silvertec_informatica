from produtos.models import MemoriaRam, PlacaDeVideo, PlacaMae, Processador
from rest_framework import serializers


class ProcessadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Processador
        fields = ['nome', 'marca','descricao']


class PlacaMaeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlacaMae
        fields = ['nome','marca', 'slots', 'memoriaSuportada', 'videoIntegrado', 'descricao']


class MemoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemoriaRam
        fields = ['nome', 'totalGigas','quantidade','descricao']


class PlacaDeVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlacaDeVideo
        fields = ['nome','descricao']
