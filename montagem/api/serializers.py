from requests import Response
from rest_framework.status import HTTP_400_BAD_REQUEST

from montagem.models import Montagem
from rest_framework import serializers, status

from produtos.models import Processador, PlacaMae, MemoriaRam, PlacaDeVideo


class MontagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Montagem
        fields = ['nome', 'processador', 'placa_mae', 'memoria', 'placa_de_video']

    def validate(self, data):
        processador = data['processador']
        placa_mae = data['placa_mae']
        memoria = data['memoria']
        placa_de_video = data['placa_de_video']

        #Validacao nao pode ser vazio
        if memoria is None:
            raise serializers.ValidationError("Voce precisa selecionar pelo menos uma memoria")
        if processador is None:
            raise serializers.ValidationError("Voce precisa selecionar pelo menos um processador")
        if placa_mae is None:
            raise serializers.ValidationError("Voce precisa selecionar pelo menos uma placa mae")

        # Validacao Processador && Placa Mae
        if not ((processador.marca == placa_mae.marca) or (
            (placa_mae.marca == placa_mae.INTEL_AMD))):
            raise serializers.ValidationError("A placa mae nao suporta esse processador")

        # Validacao Placa Mae && Memoria
        if (placa_mae.slots < memoria.quantidade):
            raise serializers.ValidationError("Essa placa mae nao tem quantidade de slots suficientes")

        if (placa_mae.memoria_suportada.tamanho < memoria.total_gigas.tamanho):
            raise serializers.ValidationError("A placa Mae nao Suporta essa quantidade de memoria")
        # Validacao da Placa de Video
        if not placa_mae.video_integrado:
            if placa_de_video is None:
                raise serializers.ValidationError(
                    "placa mae nao possui video integrado por favor escolha uma placa de video")

        return data






# Validacao Processador && Placa Mae
#         if not ((processador.marca == placamae.marca) or
#                 (placamae.marca == placamae.marca.INTEL_AMD)):
#             raise serializers.ValidationError("A placa mae nao suporta esse processador")