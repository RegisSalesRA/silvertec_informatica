from .serializers import CampoSerializer, ClientesSerializers, UsuarioTesteSerializer
from .models import Campos, Clientes, UsuarioTeste
from django.shortcuts import render
from rest_framework import viewsets, renderers
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
class CampoView(viewsets.ModelViewSet):
    queryset = Campos.objects.all()
    serializer_class = CampoSerializer


class ClienteView(viewsets.ModelViewSet):
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializers


class ClienteViewHtml(viewsets.ModelViewSet):
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializers
    template_name = 'index.html'

    def form(self, request, *args, **kwargs):
        serializer = ClientesSerializers()
        return Response({'serializer': serializer})

class UsuarioTesteView(viewsets.ModelViewSet):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'
    queryset = UsuarioTeste.objects.all()


    def get(self, request):
        queryset = UsuarioTeste.objects.all()
        return Response({'profiles': queryset})
