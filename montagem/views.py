from montagem.api.serializers import MontagemSerializer
from montagem.models import Montagem
from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
class MontagemView(viewsets.ModelViewSet):
    queryset = Montagem.objects.all()
    serializer_class = MontagemSerializer