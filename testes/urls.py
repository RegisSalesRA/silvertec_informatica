from .views import CampoView, ClienteView
from django.urls import path
from rest_framework.routers import SimpleRouter

Campo = SimpleRouter()
Campo.register('campo', CampoView)
Campo.register('cliente', ClienteView)


urlpatterns = [
    path('campo', CampoView, name='campo'),
    path('cliente', ClienteView, name='cliente'),
    ]
