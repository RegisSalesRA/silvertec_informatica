from django.db import models


# Create your models here.

class Processador(models.Model):
    marca = models.CharField(max_length=150, )


    class Meta:
        verbose_name = 'Processador'
        verbose_name_plural = "Processadores"

    def __str__(self):
        return self.nome

class PlacaMae(models.Model):
    nome = models.CharField(max_length=150, )
    processador = models.CharField()


    class Meta:
        verbose_name = 'Placa Mãe'
        verbose_name_plural = "Placas Mãe"

    def __str__(self):
        return self.nome

class MemoriaRam(models.Model):
    nome = models.CharField(max_length=150, )


    class Meta:
        verbose_name = 'Memoria Ram'
        verbose_name_plural = "Memorias"

    def __str__(self):
        return self.nome

class PlacaDeVideo(models.Model):
    nome = models.CharField(max_length=150, )


    class Meta:
        verbose_name = 'Placa de video'
        verbose_name_plural = "Placas de video"


    def __str__(self):
        return self.nome