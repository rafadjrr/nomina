from django.db import models
from apps.departamento.models import *
from ckeditor.fields import RichTextField
# Create your models here.
class Habilidad(models.Model):
    """Model definition for Habilidades."""
    name = models.CharField('habilidad', max_length=15)
    class Meta:
        """Meta definition for Habilidades."""

        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades'
    def __str__(self):
        """Unicode representation of Habilidades."""
        return self.name + str(self.id)
class Empleado(models.Model):
    """Model definition for Empleado."""
    JOB_CHOICES =(
        ('0','ingeniero informatico'),
        ('1','ingeniero sistemas'),
        ('2','electronico'),
    )
    first_name = models.CharField('nombres', max_length=60)
    last_name = models.CharField('apellidos', max_length=60)
    full_name = models.CharField('nombre completo', max_length=120, blank=True)
    jobs = models.CharField('trabajo', max_length=1,choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='empleado', height_field=None, width_field=None, max_length=None,null=True,blank=True)
    habilidades = models.ManyToManyField(Habilidad)
    historia = RichTextField()
    class Meta:
        """Meta definition for Empleado."""
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados de la empresa'
        ordering = ['jobs']
        unique_together = ('first_name','last_name','jobs')
    def __str__(self):
        """Unicode representation of Empleado."""
        return self.first_name + " " + self.last_name 