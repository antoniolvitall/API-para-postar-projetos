from django.urls import path
from portifolio.views import index

urlpatterns = [
    path('', index)
]
