from django.db import models
from utileria.models import ObraTeatro, Sala


class Pelicula(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    duracion = models.DurationField()
    realizador = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='imagen/', null=True, blank=True)

    def __str__(self):
        return self.nombre
    
class ObraSala(models.Model):
    obra_teatro = models.ForeignKey(ObraTeatro, related_name='obras_salas', on_delete=models.CASCADE, null=True, blank=True)
    pelicula = models.ForeignKey(Pelicula, related_name='peliculas_salas', on_delete=models.CASCADE, null=True, blank=True)
    sala = models.ForeignKey(Sala, related_name='obras_peliculas', on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        if self.obra_teatro:
            return f"Obra de Teatro: {self.obra_teatro.nombre} - Sala: {self.sala.nombre} - Fecha: {self.fecha}"
        elif self.pelicula:
            return f"Película: {self.pelicula.nombre} - Sala: {self.sala.nombre} - Fecha: {self.fecha}"