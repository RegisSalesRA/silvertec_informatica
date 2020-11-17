from django.db import models


# Create your models here.

class Processador(models.Model):
    INTEL = 'INTEL'
    AMD = 'AMD'

    marcas = [
        (INTEL, 'INTEL'),
        (AMD, 'AMD'),
    ]

    nome = models.CharField(max_length=100)
    marca = models.CharField(choices=marcas, max_length=100)

    class Meta:
        verbose_name = 'Processador'
        verbose_name_plural = "Processadores"

    def __str__(self):
        return f'{self.nome} {self.marca}'



class PlacaMae(models.Model):
    processador_suportado = [
        ('INTEL', 'INTEL'),
        ('AMD', 'AMD'),
        ('INTEL_AMD', 'INTEL E AMD')
    ]

    memoria_suportada = [
        ('opcao1', 'Até 16 GB'),
        ('opcao2', 'Até 64 GB'),
    ]

    nome = models.CharField(max_length=150, )
    processadorSuportado = models.CharField(choices=processador_suportado, max_length=100)
    slots = models.IntegerField(default=0)
    memoriaSuportada = models.CharField(choices=memoria_suportada, max_length=100)
    videoIntegrado = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Placa Mãe'
        verbose_name_plural = "Placas Mãe"

    def __str__(self):
        return f'{self.nome} {self.processadorSuportado} {self.memoriaSuportada} {self.videoIntegrado}'



class MemoriaRam(models.Model):
    disponiveis = [
        ('opcao1', '4 GB'),
        ('opcao2', '8 GB'),
        ('opcao3', '16 GB'),
        ('opcao4', '32 GB'),
        ('opcao5', '64 GB'),
    ]

    nome = models.CharField(max_length=150, )
    tamanho = models.CharField(choices=disponiveis, max_length=100)

    class Meta:
        verbose_name = 'Memoria Ram'
        verbose_name_plural = "Memorias"

    def __str__(self):
        return f'{self.nome} {self.tamanho}'


class PlacaDeVideo(models.Model):
    nome = models.CharField(max_length=150, )

    class Meta:
        verbose_name = 'Placa de video'
        verbose_name_plural = "Placas de video"

    def __str__(self):
        return self.nome
