from produtos.models import MemoriaRam, PlacaDeVideo, PlacaMae, Processador
from rest_framework import serializers


class ProcessadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Processador
        fields = ['id','nome', 'marca','descricao']


class PlacaMaeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlacaMae
        fields = ['id','nome','marca', 'slots', 'memoria_suportada', 'video_integrado', 'descricao']


class MemoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemoriaRam
        fields = ['id','nome', 'total_gigas','quantidade','descricao']


class PlacaDeVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlacaDeVideo
        fields = ['id','nome','descricao']
