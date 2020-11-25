from .views import CampoView, ClienteView, ClienteViewHtml, UsuarioTesteView
from django.urls import path
from rest_framework.routers import SimpleRouter

Campo = SimpleRouter()
Campo.register('campo', CampoView)
Campo.register('cliente', ClienteView)
Campo.register('clienteform', ClienteViewHtml)
Campo.register('usuarioteste', UsuarioTesteView)

urlpatterns = [
    path('campo', CampoView, name='campo'),
    path('cliente', ClienteView, name='cliente'),
    path('clienteHtml', ClienteViewHtml, name='clienteHtml'),
    path('usuarioteste', UsuarioTesteView, name='usuarioteste'),
]
