from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


from .models import Profesor
from .forms import ProfesorForm, UserRegistrationForm

# Create your views here.
def index (request):
    return render(request, 'ruta/index.html')


def formulario (request):   
    return render(request, 'ruta/formulario.html')


def create (request):
    form = ProfesorForm(request.POST or None)
    form_class = ProfesorForm
    if request.method == 'POST':
    
        form = ProfesorForm(request.POST)

        if form.is_valid():
            #print('Formulario valido')
            profesor = Profesor()
            profesor.nombre = form.cleaned_data['nombre']
            profesor.apellido = form.cleaned_data['apellido']
            profesor.edad = form.cleaned_data['edad']
            profesor.email = form.cleaned_data['email']
            profesor.fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
            profesor.save()   #Guardar en la base de datos
        else:
            print('Formulario invalido')


    return render(request, 'ruta/create.html', {'form': form})
"""
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            messages.success(request, f'Account created for {username}!')
            form.save()
            return HttpResponse('Usuario creado correctamente')
    return render(request, 'ruta/register.html', {'form': form})"""

def register(request):
    if request.method == 'POST':    
        form = UserRegistrationForm(request.POST)   
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Cuenta {username} creada exitosamente.')
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}

    return render(request, 'ruta/register.html', context)