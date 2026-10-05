from django.db import models
from djongo import models


class Contacto(models.Model):
    correo = models.EmailField(max_length=150)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=200, blank=True)
    ciudad = models.CharField(max_length=100, default='Bogota')

    class Meta:
        abstract = True


class Estudiante(models.Model):
    PROGRAMAS = [
        ('ING_SOFTWARE', 'Ingenieria de Software'),
        ('ING_INDUSTRIAL', 'Ingenieria Industrial'),
        ('ADMINISTRACION', 'Administracion de Empresas'),
        ('CONTADURIA', 'Contaduria Publica'),
        ('DISENO', 'Diseno Grafico'),
    ]

    codigo_estudiantil = models.CharField(max_length=15, unique=True)
    documento = models.CharField(max_length=15, unique=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    programa = models.CharField(max_length=20, choices=PROGRAMAS, default='ING_SOFTWARE')
    semestre = models.PositiveIntegerField(default=1)
    
    contacto = models.EmbeddedField(model_container=Contacto)
    sancionado = models.BooleanField(default=False, help_text='Si esta sancionado no puede pedir prestamos')
    activo = models.BooleanField(default=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)