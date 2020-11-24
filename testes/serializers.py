from .models import Campos, Clientes
from rest_framework import serializers


class CampoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campos
        fields = ['nome', 'idade', 'quantidade']

    def validate_idade(self, idade):
        if idade % 2 == 0:
            return idade
        raise serializers.ValidationError('O numero esta incorreto sinto muito tente novamente!')

    def validate_nome(self, nome):
        if nome == range(1, 6):
            return nome
        raise serializers.ValidationError('Nome muito cumprido!')


class ClientesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fields = ['nome', 'sobrenome']

    def validate(self, data):
        nome = data['nome']
        sobrenome = data['sobrenome']

        if nome.trabalho == sobrenome.trabalho:
            raise serializers.ValidationError("Nao pode ser o mesmo emprego")
        # elif nome.nome == sobrenome.sobrenome:
        #     raise serializers.ValidationError("Nome precisa ser diferente do sobrenome")
        return data