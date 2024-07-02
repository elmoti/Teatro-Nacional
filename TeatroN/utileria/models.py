from django.db import models

class Salas(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'salas'
    
class ObrasTeatro(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    genero = models.CharField(max_length=50, null=True, blank=True)
    sala = models.ForeignKey(Salas, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'obrasteatro'

class Utileria(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=50)
    descripcion = models.TextField()

    def __str__(self):
        return self.codigo
    
    class Meta:
        db_table = 'utileria'

class DirectorObra(models.Model):
    ci = models.CharField(max_length=11, primary_key=True)
    nombre = models.CharField(max_length=100)
    anos_experiencia = models.IntegerField()

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'directoreobras'

class ReservaUtileria(models.Model):
    id = models.AutoField(primary_key=True)
    obras = models.ForeignKey(ObrasTeatro, on_delete=models.CASCADE)
    utileria = models.ForeignKey(Utileria, on_delete=models.CASCADE)
    fecha_reserva = models.DateField()
    estado = models.CharField(max_length=20, choices=[
        ('pendiente', 'Pendiente'),
        ('aprobada', 'Aprobada'),
        ('denegada', 'Denegada'),
    ], default='pendiente')
    fecha_aprobacion = models.DateField(null=True, blank=True)
    director_obra = models.ForeignKey(DirectorObra, on_delete=models.CASCADE)

    def __str__(self):
        return f"Reserva de {self.utileria} por {self.director_obra.username}"
    
    class Meta:
        db_table = 'reservasutileria'

class Escenografo(models.Model):
    ci = models.CharField(max_length=11, primary_key=True)
    nombre = models.CharField(max_length=100)
    anios_experiencia = models.IntegerField()

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'escenografos'

class Supervision(models.Model):
    id = models.AutoField(primary_key=True)
    reserva = models.OneToOneField(ReservaUtileria, on_delete=models.CASCADE)
    escenografo = models.ForeignKey(Escenografo, on_delete=models.CASCADE)

    def __str__(self):
        return f'Supervision {self.id} - {self.escenografo.nombre}'

    class Meta:
        db_table = 'supervisiones'
