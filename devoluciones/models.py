from django.db import models
from djongo import models
from prestamos.models import Prestamo


class Devolucion(models.Model):
    ESTADOS_IMPLEMENTO = [
        ('BUENO', 'En buen estado'),
        ('DANADO', 'Danado'),
        ('INCOMPLETO', 'Incompleto'),
        ('PERDIDO', 'Perdido'),
    ]

    prestamo = models.OneToOneField(Prestamo, on_delete=models.CASCADE, related_name='devolucion')
    fecha_devolucion = models.DateTimeField(auto_now_add=True)
    estado_implemento = models.CharField(max_length=12, choices=ESTADOS_IMPLEMENTO, default='BUENO')
    dias_retraso = models.PositiveIntegerField(default=0)
    genera_sancion = models.BooleanField(default=False)
    valor_sancion = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    recibido_por = models.CharField(max_length=100)
    observaciones = models.TextField(blank=True)