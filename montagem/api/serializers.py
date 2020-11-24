from requests import Response
from rest_framework.status import HTTP_400_BAD_REQUEST

from montagem.models import Montagem
from rest_framework import serializers, status

from produtos.models import Processador, PlacaMae, MemoriaRam, PlacaDeVideo


class MontagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Montagem
        fields = ['nome','processador', 'placamae','memoria','placadevideo']

    def validate(self, data):
        processador = data['processador']
        placamae = data['placamae']
        memoria = data['memoria']
        placadevideo = data['placadevideo']

        # if processador.marca != placamae.marca:
        #     raise serializers.ValidationError("A placa mae nao suporta esse processador")

        #
        # if not ((processador.marca == placamae.marca) or (
        #         (placamae.marca == placamae.INTEL_AMD))):
        #     raise serializers.ValidationError("A placa mae nao suporta esse processador")
        #
        # if len(memoria) > 1:
        #
        #
        # return data