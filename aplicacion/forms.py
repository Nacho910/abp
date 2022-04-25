from django import forms
from django .forms import ModelForm, TextInput, NumberInput, Select, DateInput, EmailInput, PasswordInput
from django.contrib.auth.models import User
from .models import Profesor

"""
class ProfesorForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True, label="Nombre Profesor")
    apellido = forms.CharField(max_length=50, required=True, label="Apellido Profesor")
    edad = forms.IntegerField(required=True, label="Edad Profesor")
    email = forms.EmailField(max_length=254, required=True, label="Correo Electrónico")
    fecha_nacimiento = forms.DateField(required=True, label="Fecha de Nacimiento")"""
 

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ('nombre', 'apellido', 'edad', 'email', 'fecha_nacimiento')
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'control',
                'placeholder': 'Nombre Profesor',
                'style': 'max-width: 300px;',
                'label': 'nombre',
                'required': 'True',
                'max_length': '50'
                }),
            'apellido': forms.TextInput(attrs={
                'class': 'control',
                'placeholder': 'apellido',
                'style': 'max-width: 300px;',
                'label': 'Apellido Profesor',
                'required': 'True',
                'max_length': '50'
                }),
            'edad': forms.NumberInput(attrs={
                'class': 'control',
                'placeholder': 'edad',
                'style': 'max-width: 300px;',
                'label': 'Edad Profesor',
                'required': 'True',
                'max_length': '50'
                }),
            'email': forms.EmailInput(attrs={
                'class': 'control',
                'placeholder': 'email',
                'style': 'max-width: 300px;',
                'label': 'Correo Electrónico',
                'required': 'True',
                'max_length': '50'
                }),
            'fecha_nacimiento': forms.DateInput(attrs={
                'class': 'control',
                'placeholder': 'fecha_nacimiento',
                'style': 'max-width: 300px;',
                'label': 'Fecha de Nacimiento',
                'required': 'True',
                'max_length': '50'
                })
        }
      
"""
class ProfesorForm(forms.ModelForm):
    class meta:
        model = Profesor
        fields = ['nombre', 'apellido', 'edad', 'email', 'fecha_nacimiento']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre Profesor',
                'style': 'max-width: 300px;',
                'label': 'nombre',
                'required': 'True',
                'max_length': '50'
                }),
            'apellido': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'apellido',
                'style': 'max-width: 300px;',
                'label': 'Apellido Profesor',
                'required': 'True',
                'max_length': '50'
                }),
            'edad': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'edad',
                'style': 'max-width: 300px;',
                'label': 'Edad Profesor',
                'required': 'True',
                'max_length': '50'
                }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'email',
                'style': 'max-width: 300px;',
                'label': 'Correo Electrónico',
                'required': 'True',
                'max_length': '50'
                }),
            'fecha_nacimiento': forms.DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'fecha_nacimiento',
                'style': 'max-width: 300px;',
                'label': 'Fecha de Nacimiento',
                'required': 'True',
                'max_length': '50'
                })
        }"""