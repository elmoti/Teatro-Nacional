from django.urls import path
from . import views

urlpatterns = [
    path('home/cartelera', views.lista_evento, name='lista_evento'),
    path('home/cartelera/agregart', views.agregar_obrasala, name='agregar_obra_teatroc'),
    path('home/cartelera/agregarp', views.agregar_obrapelicula, name='agregar_obra_peliculac'),
    
    ]
