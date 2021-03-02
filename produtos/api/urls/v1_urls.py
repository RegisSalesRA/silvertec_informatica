from produtos.views import MemoriaView, PlacaDeVideoView, PlacaMaeView, ProcessadorView
from django.urls import path
from rest_framework.routers import SimpleRouter


Produtos = SimpleRouter()
Produtos.register('processador', ProcessadorView)
Produtos.register('placamae', PlacaMaeView)
Produtos.register('memoria', MemoriaView)
Produtos.register('placadevideo', PlacaDeVideoView)