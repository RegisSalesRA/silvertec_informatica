from django.db import models

# Create your models here.

class Tamanhos(models.Model):
    v1 = '4'
    v2 = '8'
    v3 = '16'
    v4 = '32'
    v5 = '64'

    total_memoria = [
        (v1, '4 GB'),
        (v2, '8 GB'),
        (v3, '16 GB'),
        (v4, '32 GB'),
        (v5, '64 GB'),
    ]

    tamanho = models.CharField(choices=total_memoria, max_length=100)

    class Meta:
        verbose_name = 'Tamanho'
        verbose_name_plural = 'Tamanhos'

    def __str__(self):
        return self.tamanho