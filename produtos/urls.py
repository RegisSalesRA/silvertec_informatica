from django.urls import include, path, re_path
from produtos.api.urls.v1_urls import Produtos

urlpatterns = [
    path('v1/', include(Produtos.urls)),
]