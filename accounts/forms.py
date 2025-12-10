from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={
            'placeholder': '••••••••',
            'name': 'password1'
        })
    )
    password2 = forms.CharField(
        label="Confirmar contraseña",
        widget=forms.PasswordInput(attrs={
            'placeholder': '••••••••',
            'name': 'password2'
        })
    )

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name')
        labels = {
            "username": "Nombre de usuario",
            "email": "Correo electrónico",
            "first_name": "Nombre",
            "last_name": "Apellido",
        }
        widgets = {
            'email': forms.EmailInput(attrs={
                'placeholder': 'juanperez@email.com',
                'name': 'email'
            }),
            'username': forms.TextInput(attrs={
                'placeholder': 'juanperez',
                'name': 'username'
            }),
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Juan',
                'name': 'first_name'
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Perez',
                'name': 'last_name'
            }),
        }