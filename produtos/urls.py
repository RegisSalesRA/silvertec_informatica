from produtos.views import ProcessadorView
from django.urls import path
from rest_framework.routers import SimpleRouter


Produtos = SimpleRouter()
Produtos.register('processador', ProcessadorView)


urlpatterns = [

    # API
    path('processador/', ProcessadorView, name='igrejas'),
]