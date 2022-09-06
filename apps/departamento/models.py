from django.db import models

# Create your models here.

class Departamento(models.Model):
    """Model definition for Departamento."""
    name = models.CharField('Nombre', max_length=50,unique=True)
    nick = models.CharField('Apodo', max_length=20,blank=True)
    estatus = models.BooleanField('Estatus',default=False,auto_created=True,editable=False)
    
    class Meta:
        """Meta definition for Departamento."""

        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'

    def __str__(self):
        """Unicode representation of Departamento."""
        return self.name
