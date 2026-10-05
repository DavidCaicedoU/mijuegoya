from django.db import models
from djongo import models
from estudiantes.models import Estudiante


class DetallePrestamo(models.Model):
    codigo_implemento = models.CharField(max_length=20)
    nombre_implemento = models.CharField(max_length=120)
    cantidad = models.PositiveIntegerField(default=1)
    observacion = models.CharField(max_length=200, blank=True)

    class Meta:
        abstract = True


class Prestamo(models.Model):
    ESTADOS = [
        ('ACTIVO', 'Activo'),
        ('DEVUELTO', 'Devuelto'),
        ('ATRASADO', 'Atrasado'),
        ('CANCELADO', 'Cancelado'),
    ]

    numero_prestamo = models.CharField(max_length=20, unique=True)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name='prestamos')
    detalle = models.ArrayField(model_container=DetallePrestamo)
    fecha_prestamo = models.DateTimeField(auto_now_add=True)
    fecha_estimada_devolucion = models.DateField()
    estado = models.CharField(max_length=10, choices=ESTADOS, default='ACTIVO')
    entregado_por = models.CharField(max_length=100)
    observaciones = models.TextField(blank=True)