from django import forms
from utileria.models import Utileria
from .models import ReservaUtileria

class UtileriaForm(forms.ModelForm):
    class Meta:
        model = Utileria
        fields = '__all__'
        

class ReservarUtileriaForm(forms.ModelForm):
    class Meta:
        model = ReservaUtileria
        fields = ['fecha_reserva', 'estado', 'fecha_aprobacion'] 

class AprobarReservaForm(forms.ModelForm):
    class Meta:
        model = ReservaUtileria
        fields = ['estado']
