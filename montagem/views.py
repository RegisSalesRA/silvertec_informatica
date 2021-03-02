from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from montagem.api.serializers import MontagemSerializer, UserSerializer
from montagem.models import Montagem
from django.contrib.auth.models import User


# Create your views here.
class MontagemView(viewsets.ModelViewSet):
    queryset = Montagem.objects.all()
    serializer_class = MontagemSerializer

    def get(self, request, format=None):
        montagem = Montagem.objects.all()
        serializer = MontagemSerializer(montagem, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MontagemSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UsuarioView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request):
        User = User.objects.all()
        serializer = UserSerializer(User, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)