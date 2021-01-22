from requests import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from montagem.validation import *
from montagem.models import Montagem
from rest_framework import serializers, status

from produtos.models import Processador, PlacaMae, MemoriaRam, PlacaDeVideo


class MontagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Montagem
        fields = ['nome', 'processador', 'placa_mae', 'memoria', 'placa_de_video']

    def validate(self, data):
        validar_processador_compatibilidade(data)
        validar_memoria_slot(data)
        validar_memoria_quantidade_gigas(data)
        validar_placa_de_video(data)
        
        return data






# Validacao Processador && Placa Mae
#         if not ((processador.marca == placamae.marca) or
#                 (placamae.marca == placamae.marca.INTEL_AMD)):
#             raise serializers.ValidationError("A placa mae nao suporta esse processador")