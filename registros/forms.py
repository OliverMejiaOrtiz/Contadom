from django import forms
from .models import Cuenta, Transaccion, DetalleTransaccion

class CuentaForm(forms.ModelForm):
    class Meta:
        model = Cuenta
        fields = ['id_cuenta', 'nombre_cuenta', 'id_categoria']
        labels = {
            'id_cuenta': 'Código de cuenta',
            'nombre_cuenta': 'Nombre de la cuenta',
            'id_categoria': 'Categoría'
        }
        widgets = {
            'id_cuenta': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el código de la cuenta'
            })
        }

class DetalleTransaccionForm(forms.ModelForm):
    class Meta:
        model = DetalleTransaccion
        fields = ['cuenta', 'monto', 'es_debe']
        widgets = {
            'cuenta': forms.Select(attrs={'class': 'form-select'}),
            'monto': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'es_debe': forms.HiddenInput()
        }

class TransaccionForm(forms.ModelForm):
    glosa = forms.CharField(
        max_length=200,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Descripción de la transacción'
        })
    )

    class Meta:
        model = Transaccion
        fields = ['fecha_transaccion', 'glosa']
        widgets = {
            'fecha_transaccion': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
        }
