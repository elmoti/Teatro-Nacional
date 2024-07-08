from django.db import models

class Pelicula(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    duracion = models.DurationField()
    realizador = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='imagen/', null=True, blank=True)

    def __str__(self):
        return self.nombre