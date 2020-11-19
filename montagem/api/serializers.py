from montagem.models import Montagem
from rest_framework import serializers


class MontagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Montagem
        fields = ['nome', 'processador', 'placamae', 'memoria', 'placadevideo']

    def validate(self, data):
        pass

    def placamae_compativel_processador(self, data):
        pass