from django import forms

from app.models import Traxxas


class TraxxasForm(forms.ModelForm):
    class Meta:
        model = Traxxas
        # widgets = {
        #     'image': forms.FileInput(attrs={'class': 'custom-file-input'}),
        # }
        fields = '__all__'


class DeleteTraxxasForm(TraxxasForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = True
            field.widget.attrs['readonly'] = True
