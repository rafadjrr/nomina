from django.db import models

# Create your models here.

class Prueba(models.Model):
    titulo = models.CharField(max_length=50)
    subitulo = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    class Meta:
        """Meta definition for MODELNAME."""

        verbose_name = 'registros de pruebas'
        verbose_name_plural = 'pruebas'

    def __str__(self):
        return self.titulo + "-" + str(self.cantidad)
