from django.db import models

# Create your models here.

class Tamanhos(models.Model):
    disponiveis = [
        ('4 GB', '4 GB'),
        ('8 GB', '8 GB'),
        ('16 GB', '16 GB'),
        ('32 GB', '32 GB'),
        ('64 GB', '64 GB'),
    ]

    tamanho = models.CharField(choices=disponiveis, max_length=100)

    class Meta:
        verbose_name = 'Tamanho'
        verbose_name_plural = 'Tamanhos'

    def __str__(self):
        return self.tamanho


class Marcas(models.Model):
    marcas_opcoes = [
        ('INTEL', 'INTEL'),
        ('AMD', 'AMD'),
        ('INTEL_AMD', 'INTEL E AMD')
    ]
    marcas = models.CharField(max_length=100, choices=marcas_opcoes)

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

    def __str__(self):
        return self.marcas

