from requests import Response
from rest_framework.status import HTTP_400_BAD_REQUEST

from montagem.models import Montagem
from rest_framework import serializers, status

from produtos.models import Processador, PlacaMae, MemoriaRam, PlacaDeVideo


class MontagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Montagem
        fields = ['processador', 'placamae']

        def validate(self, data):
            processadores = data['processador']
            placasmae = data['placamae']
            # memoria = data['memoria']
            # placadevideo = data['placadevideo']

            # try:
            #     processador = Processador.objects.get(pk=processadores)
            # except Processador.DoesNotExist:
            #

            if not processadores.marca == placasmae.marca:
                raise serializers.ValidationError("A placa mae nao suporta esse processador")
            return data
