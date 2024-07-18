from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('acercade/', views.acercade, name='acercade'),
    
    path('utilerias/', views.listar_utilerias, name='listar_utilerias'),
    path('utilerias/<int:utileria_id>/', views.detalle_utileria, name='detalle_utileria'),
    path('utilerias/agregar/', views.agregar_utileria, name='agregar_utileria'),
    path('utilerias/eliminar/<int:utileria_id>', views.eliminar_utileria, name='eliminar_utileria'),
    path('utilerias/editar/<int:utileria_id>', views.editar_utileria, name='editar_utileria'),
    path('utilerias/reservar/<int:utileria_id>', views.reservar_utileria, name='reservar_utileria'),
    
    path('lista_reserva_utileria', views.lista_reserva_utileria, name='lista_reserva_utileria'),
    path('lista_reserva_utileria/editar/<int:reserva_id>/', views.editar_reserva, name='editar_reserva'),
    path('lista_reserva_utileria/eliminar/<int:reserva_id>/', views.eliminar_reserva, name='eliminar_reserva'),
]
