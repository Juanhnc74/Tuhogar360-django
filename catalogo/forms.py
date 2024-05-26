from .models import Propiedad
from django import forms

class PropiedadForm(forms.ModelForm):
    class Meta:
        model = Propiedad
        fields = ['direccion', 'precio', 'area', 'num_habitaciones', 'num_baños', 'imagen_principal', 'imagen_principal', 'descripcion']
        widgets = {
            'fecha_publicacion': forms.DateInput(attrs={'type': 'date'}),
        }
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.user = user

    def save(self, commit=True):
        propiedad = super().save(commit=False)
        propiedad.usuario = self.user
        if commit:
            propiedad.save()
        return propiedad
    

class BusquedaForm(forms.Form):
    query = forms.CharField(label='', max_length=255, required=False, widget=forms.TextInput(attrs={'placeholder': 'Buscar...'}))