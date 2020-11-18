from .serializers import CampoSerializer
from .models import Campos
from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
class CampoView(viewsets.ModelViewSet):
    queryset = Campos.objects.all()
    serializer_class = CampoSerializer