from django.urls import include, path, re_path
from montagem.api.urls.v1_urls import Usuario, Montagem

urlpatterns = [
    path('v1/', include(Usuario.urls)),
    path('v1/', include(Montagem.urls)),
]