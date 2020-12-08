from django import forms

from app.models import Traxxas


class TraxxasForm(forms.ModelForm):
    class Meta:
        model = Traxxas
        # widgets = {
        #     'image': forms.FileInput(attrs={'class': 'custom-file-input'}),
        # }
        fields = '__all__'

