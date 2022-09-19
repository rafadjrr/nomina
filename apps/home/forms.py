from django import forms
from .models import *

class PruebaForm(forms.ModelForm):
    """Form definition for Prueba."""

    class Meta:
        """Meta definition for Pruebaform."""

        model = Prueba
        fields = (
            'titulo',
            'subitulo',
            'cantidad',
        )
        widgets = {
            'titulo':forms.TextInput(
                attrs={
                    'placeholder': 'ingrese texto'
                }
            ),
            'subitulo':forms.TextInput(
                attrs={
                    'placeholder': 'ingrese texto'
                }
            )
        }

    def clean_cantidad(self):
        cantidad = self.cleaned_data.get('cantidad')
        if cantidad < 10:
            # TODO Validation
            raise forms.ValidationError('ingrese un numero mayor a 10')
        return cantidad
