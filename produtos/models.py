from django.db import models

# Create your models here.

class Processador(models.Model):
    nome = models.CharField(max_length=150,)


class PlacaMae(models.Model):
    nome = models.CharField(max_length=150,)


class MemoriaRam(models.Model):
    nome = models.CharField(max_length=150,)


class PlacaDeVideo(models.Model):
    nome = models.CharField(max_length=150,)