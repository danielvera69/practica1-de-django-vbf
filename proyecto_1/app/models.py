from django.db import models
from django.utils import timezone


class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=200)
    mail = models.EmailField()
    prueba = models.BooleanField(default=True)
    creacion = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha Creacion")
    modificacion = models.DateTimeField(
        auto_now=True, verbose_name="Fecha Modificacion")

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'
        ordering = ["-creacion"]

    def __str__(self):
        return self.nombre


class Entrada(models.Model):
    contacto = models.ForeignKey(Contacto, on_delete=models.CASCADE)
    descripcion = models.TextField()
    fecha = models.DateTimeField(default=timezone.datetime.now())
    creacion = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha Creacion")
    modificacion = models.DateTimeField(
        auto_now=True, verbose_name="Fecha Modificacion")

    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'
        ordering = ["-creacion"]

    def __str__(self):
        return self.descripcion
