from requests import Response
from rest_framework.status import HTTP_400_BAD_REQUEST

from montagem.models import Montagem
from rest_framework import serializers, status

from produtos.models import Processador, PlacaMae, MemoriaRam, PlacaDeVideo


class MontagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Montagem
        fields = ['nome', 'processador', 'placamae', 'memoria', 'placadevideo']

    def validate(self, data):
        processador = data['processador']
        placamae = data['placamae']
        memoria = data['memoria']
        placadevideo = data['placadevideo']

        # Validacao Processador && Placa Mae
        if not ((processador.marca == placamae.marca) or (
                (placamae.marca == placamae.INTEL_AMD))):
            raise serializers.ValidationError("A placa mae nao suporta esse processador")

        # Validacao Placa Mae && Memoria
        if (placamae.slots < memoria.quantidade):
            raise serializers.ValidationError("Essa placa mae nao tem quantidade de slots suficientes")

        if (placamae.memoriaSuportada < memoria.totalGigas):
            raise serializers.ValidationError("A placa Mae nao Suporta essa quantidade de memoria")
        # Validacao da Placa de Video
        if not placamae.videoIntegrado:
            if placadevideo is None:
                raise serializers.ValidationError("placa mae nao possui video integrado por favor escolha uma placa de video")

        return data