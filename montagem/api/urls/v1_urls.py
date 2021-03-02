from montagem.views import MontagemView, UsuarioView
from django.urls import path
from rest_framework.routers import SimpleRouter


Montagem = SimpleRouter()
Montagem.register('montagens', MontagemView)

Usuario = SimpleRouter()
Usuario.register('users', UsuarioView)