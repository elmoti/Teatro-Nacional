from django import forms
from utileria.models import Utileria

class UtileriaForm(forms.ModelForm):
    class Meta:
        model = Utileria
        fields = '__all__'
