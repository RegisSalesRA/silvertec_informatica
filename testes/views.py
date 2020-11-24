from .serializers import CampoSerializer, ClientesSerializers
from .models import Campos, Clientes
from django.shortcuts import render
from rest_framework import viewsets
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


class ClienteViewHtml(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'
    #serializer_class = ClientesSerializers

    def get(self, request, *args,**kwargs):
        queryset = Clientes.objects.all()
        return Response(request,{'clientes': queryset})
