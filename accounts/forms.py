from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label="Confirmar contraseña",
        widget=forms.PasswordInput
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