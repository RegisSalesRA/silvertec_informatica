from montagem.views import MontagemView, UsuarioView
from django.urls import path
from rest_framework.routers import SimpleRouter


Montagem = SimpleRouter()
Montagem.register('', MontagemView)

Usuario = SimpleRouter()
<<<<<<< HEAD
Usuario.register('users', UsuarioView)
=======
Usuario.register('', UsuarioView)

urlpatterns = [
    path('', MontagemView, name='montagem'),
]
>>>>>>> 5a0437eda0d593724fe3d0d137aabc65e99e8033
