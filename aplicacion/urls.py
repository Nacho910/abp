from django.urls import URLPattern, path, include
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('formulario/', views.formulario, name='formulario'),
    path('create/', views.create, name='create'),
    path('register/', views.register, name='register'),
    
]
