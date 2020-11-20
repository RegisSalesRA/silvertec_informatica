from django.db import models


# Create your models here.

class Campos(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField(default=0)
    quantidade = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Campo'
        verbose_name_plural = 'Campos'

    def __str__(self):
        return self.nome


class Nome(models.Model):
    nome = models.CharField(max_length=100)
    ativo = models.BooleanField(default=False)

    def __str__(self):
        return self.nome


class Sobrenome(models.Model):
    sobrenome = models.CharField(max_length=100)
    ativo = models.BooleanField(default=False)

    def __str__(self):
        return self.sobrenome


class Clientes(models.Model):
    nome = models.ForeignKey(Nome, on_delete=models.CASCADE)
    sobrenome = models.ForeignKey(Sobrenome, on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return str(self.nome)

#
# class Keys_Serializer(serializers.Serializer):
#
#     key_id = serializers.IntegerField(required=True)
#     key_name = serializers.CharField(required=True)
#     value_id = serializers.IntegerField(required=False)
#
#     def validate(self, data):
#         # here you can access all values
#         key_id = data['key_id']
#         value_id = data['value_id']
#         # perform you validation
#         if key_id != value_id:
#             raise serializers.ValidationError("key_id must be equal to value_id")
#         return data
