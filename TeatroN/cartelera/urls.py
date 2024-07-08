from django.urls import path
from . import views

urlpatterns = [
    path('home/obras', views.listar_obra, name='listar_obra'),
    path('home/obras/agregar', views.agregar_obra_teatro, name='agregar_obra_teatro'),
    path('home/obras/editar_obra/<int:obra_id>/', views.editar_obra, name='editar_obra'),
    path('home/obras/eliminar_obra/<int:obra_id>/', views.eliminar_obra, name='eliminar_obra'),
    
    path('home/peliculas', views.listar_pelicula, name='listar_pelicula'),
    path('home/pelicula/agregar', views.agregar_pelicula, name='agregar_pelicula'),
    path('home/peliculas/editar_pelicula/<int:pelicula_id>/', views.editar_pelicula, name='editar_pelicula'),
    path('home/pelicula/eliminar_pelicula/<int:pelicula_id>/', views.eliminar_pelicula, name='eliminar_pelicula'),
]