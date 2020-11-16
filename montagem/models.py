from django.db import models
from produtos.models import Processador,PlacaDeVideo,PlacaMae,MemoriaRam
# Create your models here.


class Montagem(models.Model):
    nome = models.CharField(max_length=100)
    processador = models.ForeignKey(Processador , on_delete=models.CASCADE)
    placamae = models.ForeignKey(PlacaMae , on_delete=models.CASCADE)
    memoria = models.ForeignKey(MemoriaRam , on_delete=models.CASCADE)
    placadevideo = models.ForeignKey(PlacaDeVideo , on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Montagem'
        verbose_name_plural = 'Montagens'
    
    def __str__(self):
        return self.nome