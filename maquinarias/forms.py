from django import forms
from .models import Maquinaria, CategoriaFaena

class MaquinariaForm(forms.ModelForm):
    class Meta:
        model = Maquinaria
        fields = [
            'codigo', 'nombre', 'categoria', 'descripcion',
            'precio_arriendo_dia', 'precio_venta', 'garantia_requerida',
            'stock', 'estado', 'tipo_oferta', 'imagen', 'destacado'
        ]
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: EXC-005'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Mini Excavadora Bobcat'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'precio_arriendo_dia': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'precio_venta': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'garantia_requerida': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'stock': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
            'tipo_oferta': forms.Select(attrs={'class': 'form-select'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'destacado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }