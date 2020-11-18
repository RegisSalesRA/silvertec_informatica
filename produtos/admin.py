from django.contrib import admin
from .models import Processador, PlacaMae, PlacaDeVideo, MemoriaRam

# Register your models here.

admin.site.register(Processador)
admin.site.register(PlacaMae)
admin.site.register(MemoriaRam)
admin.site.register(PlacaDeVideo)
