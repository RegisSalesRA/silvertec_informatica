from produtos.models import MemoriaRam, PlacaDeVideo, PlacaMae, Processador
from rest_framework import serializers


class ProcessadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Processador
        fields = "__all__"


class PlacaMaeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlacaMae
        fields = "__all__"


class MemoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemoriaRam
        fields = "__all__"


class PlacaDeVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlacaDeVideo
        fields = "__all__"