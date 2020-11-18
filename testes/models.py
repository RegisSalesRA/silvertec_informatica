from django.db import models

# Create your models here.

class Campos(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField(default=0)
    quantidade = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Campo'
        verbose_name_plural = 'Campos'

    def __str__(self):
        return self.nome