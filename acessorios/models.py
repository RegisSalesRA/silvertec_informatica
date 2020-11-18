from django.db import models


# Create your models here.

class Cores(models.Model):
    cores = [
        ('Padrao', 'Padrao'),
        ('Azul', 'azul'),
        ('Branco', 'branco'),
        ('Preto', 'preto'),
        ('Vermelho', 'Vermelho'),
    ]

    cor = models.CharField(choices=cores, max_length=100)

    class Meta:
        verbose_name = 'Cor'
        verbose_name_plural = 'Cores'

    def __str__(self):
        return self.cor