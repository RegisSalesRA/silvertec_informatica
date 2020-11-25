from django.contrib import admin
from .models import Campos, Clientes, Nome, Sobrenome, UsuarioTeste

# Register your models here.
admin.site.register(Campos)
admin.site.register(Clientes)
admin.site.register(Nome)
admin.site.register(Sobrenome)
admin.site.register(UsuarioTeste)