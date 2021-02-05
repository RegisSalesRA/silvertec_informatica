from produtos.api.serializers import MemoriaSerializer, PlacaDeVideoSerializer, PlacaMaeSerializer, ProcessadorSerializer
from produtos.models import Processador, PlacaMae, PlacaDeVideo,MemoriaRam
from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
class ProcessadorView(viewsets.ModelViewSet):
    queryset = Processador.objects.all()
    serializer_class = ProcessadorSerializer

    
class PlacaMaeView(viewsets.ModelViewSet):
    queryset = PlacaMae.objects.all()
    serializer_class = PlacaMaeSerializer


class MemoriaView(viewsets.ModelViewSet):
    queryset = MemoriaRam.objects.all()
    serializer_class = MemoriaSerializer


class PlacaDeVideoView(viewsets.ModelViewSet):
    queryset = PlacaDeVideo.objects.all()
    serializer_class = PlacaDeVideoSerializer

    def get(self, request, format=None):
        placa_de_video = PlacaDeVideo.objects.all()
        serializer = PlacaDeVideoSerializer(placa_de_video, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PlacaDeVideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)