from django.db import models
from informacoes.models import Tamanhos
from acessorios.models import Cores


# Create your models here.

class Processador(models.Model):
    INTEL = 'INTEL'
    AMD = 'AMD'
    INTEL_AMD = 'INTEL E AMD'

    marcas_opcoes = [
        (INTEL, 'INTEL'),
        (AMD, 'AMD'),
        (INTEL_AMD, 'INTEL E AMD')
    ]

    nome = models.CharField(max_length=100)
    marca = models.CharField(max_length=100, choices=marcas_opcoes)
    descricao = models.CharField(max_length=150)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Processador'
        verbose_name_plural = "Processadores"

    def __str__(self):
        return self.descricao


class PlacaMae(models.Model):
    INTEL = 'INTEL'
    AMD = 'AMD'
    INTEL_AMD = 'INTEL E AMD'

    marcas_opcoes = [
        (INTEL, 'INTEL'),
        (AMD, 'AMD'),
        (INTEL_AMD, 'INTEL E AMD')
    ]

    nome = models.CharField(max_length=150)
    marca = models.CharField(max_length=100, choices=marcas_opcoes)
    slots = models.IntegerField(default=0)
    memoria_suportada = models.ForeignKey(Tamanhos, on_delete=models.CASCADE)
    video_integrado = models.BooleanField(default=False)
    cor = models.ForeignKey(Cores, on_delete=models.CASCADE, blank=True, null=True)
    descricao = models.CharField(max_length=150)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Placa Mãe'
        verbose_name_plural = "Placas Mãe"

    def __str__(self):
        return self.descricao


class MemoriaRam(models.Model):
    nome = models.CharField(max_length=150)
    total_gigas = models.ForeignKey(Tamanhos, on_delete=models.CASCADE)
    cor = models.CharField(max_length=100, blank=True, null=True)
    quantidade = models.IntegerField(default=0)
    descricao = models.CharField(max_length=150)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Memoria'
        verbose_name_plural = "Memorias"

    def __str__(self):
        return self.descricao


class PlacaDeVideo(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.CharField(max_length=150)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Placa de video'
        verbose_name_plural = "Placas de video"

    def __str__(self):
        return self.descricao