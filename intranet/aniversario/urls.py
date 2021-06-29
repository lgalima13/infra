from django.urls import path
from .import views

urlpatterns = [
    path('', views.ListaAniversariante, name='ListaAniversariante'),
]