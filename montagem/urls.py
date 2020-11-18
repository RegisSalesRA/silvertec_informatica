from montagem.views import MontagemView
from django.urls import path
from rest_framework.routers import SimpleRouter


Montagem = SimpleRouter()
Montagem.register('montagem', MontagemView)


urlpatterns = [
    path('', MontagemView, name='montagem'),
]