from django.db import models
from django.contrib.auth.models import User
from produtos.models import Processador, PlacaDeVideo, PlacaMae, MemoriaRam


# Create your models here.


class Montagem(models.Model):
    usuario_id = models.ForeignKey(User, on_delete=models.CASCADE)
    processador_id = models.ForeignKey(Processador, on_delete=models.CASCADE,blank=True,null=True)
    placa_mae_id = models.ForeignKey(PlacaMae, on_delete=models.CASCADE,blank=True,null=True)
    memoria_id = models.ManyToManyField(MemoriaRam)
    placa_de_video_id = models.ForeignKey(PlacaDeVideo, on_delete=models.CASCADE, blank=True, null=True)
  
    class Meta:
        verbose_name = 'Montagem'
        verbose_name_plural = 'Montagens'

    def __str__(self):
        return f'Nome do Cliente "{self.usuario_id}" -> PEDIDO: {self.processador_id} {self.placa_mae_id} {self.memoria_id} {self.placa_de_video_id}'