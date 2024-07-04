from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('acercade/', views.acercade, name='acercade'),
    path('utilerias/', views.listar_utilerias, name='listar_utilerias'),
    path('utilerias/<int:utileria_id>/', views.detalle_utileria, name='detalle_utileria'),
    path('utilerias/agregar/', views.agregar_utileria, name='agregar_utileria'),
    path('utilerias/<int:utileria_id>/editar/', views.editar_utileria, name='editar_utileria'),
    path('utilerias/<int:utileria_id>/reservar/', views.reservar_utileria, name='reservar_utileria'),
]
