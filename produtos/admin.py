from django.contrib import admin
from .models import Marcas, Processador, PlacaMae, PlacaDeVideo, MemoriaRam, Tamanhos

# Register your models here.

admin.site.register(Processador)
admin.site.register(PlacaMae)
admin.site.register(MemoriaRam)
admin.site.register(PlacaDeVideo)
admin.site.register(Tamanhos)
admin.site.register(Marcas)