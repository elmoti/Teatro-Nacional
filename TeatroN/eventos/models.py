from django.db import models
from utileria.models import ObraTeatro, Sala
from cartelera.models import Pelicula

class ObraSala(models.Model):
    obra_teatro = models.ForeignKey(ObraTeatro, related_name='obras_salas', on_delete=models.CASCADE, null=True, blank=True)
    pelicula = models.ForeignKey(Pelicula, related_name='peliculas_salas', on_delete=models.CASCADE, null=True, blank=True)
    sala = models.ForeignKey(Sala, related_name='obras_peliculas', on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        if self.obra_teatro:
            return f"Obra de Teatro: {self.obra_teatro.nombre} - Sala: {self.sala.nombre} - Fecha: {self.fecha} - Hora: {self.hora}"
        elif self.pelicula:
            return f"Película: {self.pelicula.nombre} - Sala: {self.sala.nombre} - Fecha: {self.fecha} - Hora: {self.hora}"
