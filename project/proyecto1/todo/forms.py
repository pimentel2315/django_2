from django import forms
from .models import Tarea, Nombre

class TareaForm(forms.ModelForm):
    
    class Meta:
        model = Tarea
        fields = ['tarea']

class NombreForm(forms.ModelForm):
    
    class Meta:
        model = Nombre
        fields = ['nombre']