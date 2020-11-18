from .views import CampoView
from django.urls import path
from rest_framework.routers import SimpleRouter


Campo = SimpleRouter()
Campo.register('', CampoView)


urlpatterns = [
    path('', CampoView, name='campo'),
]