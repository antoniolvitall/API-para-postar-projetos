from django.urls import path
from portifolio.views import index, imagem

urlpatterns = [
    path('', index, name='index'),
    path('imagem/', imagem, name='imagem'),
]
