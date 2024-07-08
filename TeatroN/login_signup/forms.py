from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

        
class RegistroForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Requerido. Ingrese un correo válido.')
    nombre = forms.CharField(max_length=100, help_text='Requerido. Ingrese su nombre completo.')

    class Meta:
        model = Usuario
        fields = ('nombre', 'email', 'password1', 'password2')
        
    def save(self, commit=True):
        user = super(RegistroForm, self).save(commit=False)
        user.username = self.cleaned_data['email']  
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    username = forms.EmailField(label='Email', max_length=254, widget=forms.EmailInput(attrs={
        'placeholder': 'Correo Electrónico'
        }))
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.PasswordInput(attrs={'placeholder': 'Contraseña'})
