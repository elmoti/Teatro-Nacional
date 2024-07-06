from django import forms
from utileria.models import ReservaUtileria


class ReservaUtileriaForm(forms.ModelForm):
    class Meta:
        model = ReservaUtileria
        fields = ['estado']
