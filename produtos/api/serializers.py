from produtos.models import MemoriaRam, PlacaDeVideo, PlacaMae, Processador
from rest_framework import serializers


class ProcessadorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Processador
        fields = ['nome','marca']



class PlacaMaeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlacaMae
        fields = ['nome','processadorSuportado','slots','memoriaSuportada','videoIntegrado']



class MemoriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MemoriaRam
        fields = ['nome','tamanho']



class PlacaDeVideoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlacaDeVideo
        fields = ['nome']



