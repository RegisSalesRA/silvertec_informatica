from django.contrib import admin

# Register your models here.
from .models import Tamanhos, Marcas

admin.site.register(Marcas)
admin.site.register(Tamanhos)