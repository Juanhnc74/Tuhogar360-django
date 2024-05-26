from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label='Correo Electrónico', widget=forms.EmailInput(attrs={'class': 'form-control'}))  
    username = forms.CharField(label='Usuario', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = CustomUser
        fields = ("username", "email", "password1", "password2")

    def clean_password2(self):
        # Verifica que las contraseñas coincidan
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2
    

class LoginForm(forms.Form):
    correo = forms.EmailField(label='Correo Electrónico')
    contrasena = forms.CharField(widget=forms.PasswordInput, label='Contraseña')
# usuarios/forms.py
class RegistroForm(forms.Form):
    nombre_completo = forms.CharField(label='Nombre completo')
    correo = forms.EmailField(label='Correo Electrónico')
    usuario = forms.CharField(label='Usuario')
    contrasena = forms.CharField(widget=forms.PasswordInput, label='Contraseña')


class PerfilForm(forms.ModelForm):
    username = forms.CharField(label='Usuario', widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = CustomUser
        fields = [ 'username', 'first_name', 'last_name', 'email',]

    def __init__(self, *args, **kwargs):
        super(PerfilForm, self).__init__(*args, **kwargs)
        # Personaliza los widgets si es necesario
      # Por ejemplo, puedes añadir una clase de datepicker para usar un selector de fecha

''' 
class VendedorForm(forms.ModelForm):
    class Meta:
        model = Vendedor
        fields = ['curp', 'rfc', 'identificacion']  # Agrega 'user' al formulario

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Obtén el usuario de los argumentos de la función
        super().__init__(*args, **kwargs)
        self.user = user  # Guarda el usuario en el formulario

    def save(self, commit=True):
        vendedor = super().save(commit=False)
        vendedor.user = self.user
        if commit:
            vendedor.save()
        return vendedor
'''
    