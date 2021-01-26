from montagem.api.serializers import MontagemSerializer, UserSerializer
from montagem.models import Montagem
from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User


# Create your views here.
class MontagemView(viewsets.ModelViewSet):
    queryset = Montagem.objects.all()
    serializer_class = MontagemSerializer

class UsuarioView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer