from django import forms

from .models import *

class EmpleadoForm(forms.ModelForm):
    """Form definition for Empleado."""

    class Meta:
        """Meta definition for Empleadoform."""

        model = Empleado
        fields = (
            'first_name',
            'last_name',
            'jobs',
            'departamento',
            'avatar',
            'habilidades',
            'historia',
        )
        widgets = {
            'habilidades': forms.CheckboxSelectMultiple(

            )
        }
