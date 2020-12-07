from django import forms

from app.models import Traxxas


class TraxxasForm(forms.ModelForm):
    class Meta:
        model = Traxxas
        fields = '__all__'

