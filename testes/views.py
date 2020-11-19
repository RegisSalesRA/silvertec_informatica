from .serializers import CampoSerializer, ClientesSerializers
from .models import Campos, Clientes
from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
class CampoView(viewsets.ModelViewSet):
    queryset = Campos.objects.all()
    serializer_class = CampoSerializer

class ClienteView(viewsets.ModelViewSet):
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializers