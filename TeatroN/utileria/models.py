from django.db import models
from django.contrib.auth import get_user_model

class Sala(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'salas'


class Asiento(models.Model):
    id = models.AutoField(primary_key=True)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    fila = models.CharField(max_length=5)
    numero = models.IntegerField()

    def __str__(self):
        return f"Fila {self.fila} - Asiento {self.numero}"

    class Meta:
        db_table = 'asientos'

class ObraTeatro(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    genero = models.CharField(max_length=50, null=True, blank=True)
    imagen = models.ImageField(upload_to='imagen/', null=True, blank=True)
    
    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'obras_teatro'


class Utileria(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=50)
    descripcion = models.TextField()

    def __str__(self):
        return self.codigo

    class Meta:
        db_table = 'utileria'


class ReservaUtileria(models.Model):
    id = models.AutoField(primary_key=True)
    obra = models.ForeignKey(ObraTeatro, on_delete=models.CASCADE)
    utileria = models.ForeignKey(Utileria, on_delete=models.CASCADE)
    director_obra = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    fecha_reserva = models.DateField()
    fecha_aprobacion = models.DateField(null=True, blank=True)
    choice =[
        ('pendiente', 'Pendiente'),
        ('aprobada', 'Aprobada'),
        ('denegada', 'Denegada'),
    ]
    estado = models.CharField(max_length=20, choices=choice, default='pendiente')

    def __str__(self):
        return f"Reserva de {self.utileria.codigo} para {self.obra.nombre}"

    class Meta:
        db_table = 'reservas_utileria'
