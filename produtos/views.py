from produtos.api.serializers import ProcessadorSerializer
from produtos.models import Processador
from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
class ProcessadorView(viewsets.ModelViewSet):
    queryset = Processador.objects.all()
    serializer_class = ProcessadorSerializer