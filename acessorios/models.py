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

class Coolers(models.Model):
    magic_lights = [
        ('Padrao', 'Padrao'),
        ('Azul', 'azul'),
        ('Branco', 'branco'),
        ('Preto', 'preto'),
        ('Vermelho', 'Vermelho'),
        ('Colorido', 'Colorido')
    ]

    cor = models.CharField(choices=magic_lights, max_length=100)

    class Meta:
        verbose_name = 'Cor'
        verbose_name_plural = 'Cores'

    def __str__(self):
        return self.cor        