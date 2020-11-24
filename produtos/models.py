from django.db import models
from informacoes.models import Marcas, Tamanhos
from acessorios.models import Cores
from django.db.models.deletion import CASCADE
from django.db.models.fields.related_descriptors import create_forward_many_to_many_manager


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

    opcao1 = '16'
    opcao2 = '64'

    totalMemoria = [
        (opcao1, 'Até 16 GB'),
        (opcao2, 'Até 64 GB'),
    ]

    nome = models.CharField(max_length=150)
    marca = models.CharField(max_length=100, choices=marcas_opcoes)
    slots = models.IntegerField(default=0)
    memoriaSuportada = models.CharField(choices=totalMemoria, max_length=100)
    videoIntegrado = models.BooleanField(default=False)
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

    opcao1 = '4'
    opcao2 = '8'
    opcao3 = '16'
    opcao4 = '32'
    opcao5 = '64'

    totalMemoria = [
        (opcao1, '4 GB'),
        (opcao2, '8 GB'),
        (opcao3, '16 GB'),
        (opcao4, '32 GB'),
        (opcao5, '64 GB'),
    ]

    nome = models.CharField(max_length=150)
    totalGigas = models.CharField(max_length=100,choices=totalMemoria)
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
    none = models.BooleanField(default=False)
    descricao = models.CharField(max_length=150)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Placa de video'
        verbose_name_plural = "Placas de video"

    def __str__(self):
        return self.descricao
