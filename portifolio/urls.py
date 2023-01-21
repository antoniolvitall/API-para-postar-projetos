from django.urls import path
from portifolio.views import index, imagem

urlpatterns = [
    path('', index),
    path('imagem/', imagem)
]
