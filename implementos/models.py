from django.db import models
from djongo import models


class Ubicacion(models.Model):
    sede = models.CharField(max_length=100)
    bodega = models.CharField(max_length=50)
    estante = models.CharField(max_length=20, blank=True)

    class Meta:
        abstract = True


class Implemento(models.Model):
    CATEGORIAS = [
        ('DEPORTIVO', 'Implemento deportivo'),
        ('MESA', 'Juego de mesa'),
        ('ELECTRONICO', 'Juego electronico'),
        ('OTRO', 'Otro'),
    ]
    ESTADOS = [
        ('DISPONIBLE', 'Disponible'),
        ('AGOTADO', 'Agotado'),
        ('MANTENIMIENTO', 'En mantenimiento'),
        ('BAJA', 'Dado de baja'),
    ]

    codigo = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=120, db_index=True)
    descripcion = models.TextField(blank=True)
    categoria = models.CharField(max_length=15, choices=CATEGORIAS, default='DEPORTIVO')
    estado = models.CharField(max_length=15, choices=ESTADOS, default='DISPONIBLE')
    cantidad_total = models.PositiveIntegerField(default=1)
    cantidad_disponible = models.PositiveIntegerField(default=1)
    valor_reposicion = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    dias_maximo_prestamo = models.PositiveIntegerField(default=3)
    ubicacion = models.EmbeddedField(model_container=Ubicacion)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)