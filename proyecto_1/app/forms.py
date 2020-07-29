from django import forms
from .models import Contacto


class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ('nombre', 'telefono', 'mail')
        label = {'nombre': 'Contacto', 'telefono': 'Telefono', 'mail': 'Mail'}
