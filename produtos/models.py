from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related_descriptors import create_forward_many_to_many_manager

# Create your models here.

class Tamanhos(models.Model):

    disponiveis = [
        ('4 GB', '4 GB'),
        ('8 GB', '8 GB'),
        ('16 GB', '16 GB'),
        ('32 GB', '32 GB'),
        ('64 GB', '64 GB'),
    ]
    tamanho = models.CharField(choices=disponiveis,max_length=100)

    class Meta:
        verbose_name = 'Tamanho'
        verbose_name_plural = 'Tamanhos'

    def __str__(self):
        return self.tamanho



class Marcas(models.Model):
    processador_suportado = [
        ('INTEL', 'INTEL'),
        ('AMD', 'AMD'),
        ('INTEL_AMD', 'INTEL E AMD')
    ]
    marcas = models.CharField(max_length=100, choices=processador_suportado)


    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

    def __str__(self):
        return self.marcas


class Processador(models.Model):
    
    nome = models.CharField(max_length=100)
    marca = models.ForeignKey(Marcas, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Processador'
        verbose_name_plural = "Processadores"

    def __str__(self):
        return f'{self.nome} {self.marca}'



class PlacaMae(models.Model):

    memoria_suportada = [
        ('opcao1', 'Até 16 GB'),
        ('opcao2', 'Até 64 GB'),
    ]

    slots = [
        ('2', '2'),
        ('4', '4'),
    ]

    nome = models.CharField(max_length=150)
    marca = models.ForeignKey(Marcas, on_delete=models.CASCADE)
    slots = models.CharField(choices=slots, max_length=20)
    memoriaSuportada = models.CharField(choices=memoria_suportada, max_length=100)
    videoIntegrado = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Placa Mãe'
        verbose_name_plural = "Placas Mãe"

    def __str__(self):
        return f'{self.nome} {self.processadorSuportado} {self.memoriaSuportada} {self.videoIntegrado}'



class MemoriaRam(models.Model):

    nome = models.CharField(max_length=150)
    tamanho = models.ForeignKey(Tamanhos, on_delete=CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = 'Memoria Ram'
        verbose_name_plural = "Memorias"

    def __str__(self):
        return f'{self.nome} {self.tamanho}'


class PlacaDeVideo(models.Model):
    nome = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Placa de video'
        verbose_name_plural = "Placas de video"

    def __str__(self):
        return self.nome
