from requests import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from montagem.validation import *
from montagem.models import Montagem
from rest_framework import serializers, status
from django.contrib.auth.models import User
from produtos.models import Processador, PlacaMae, MemoriaRam, PlacaDeVideo


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')

class MontagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Montagem
        fields = ['id','usuario_id', 'processador_id', 'placa_mae_id', 'memoria_id', 'placa_de_video_id']

    def validate(self, data):
        validar_processador_compatibilidade(data)
        #validar_memoria_slot(data)
        #validar_memoria_quantidade_gigas(data)
        validar_placa_de_video(data)
        
        return data
