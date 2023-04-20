from django import forms
from .models import Training

class TrainingForm(forms.ModelForm):
    class Meta:
        model = Training
        fields = ['name', 'type', 'date_start', 'date_end', 'city', 'street_address', 'resources']
        widgets = {
                    'date_start': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
                    'date_end': forms.DateInput(attrs={'class': 'form-control',  'type': 'date'}),
                    'type': forms.Select(attrs={'class': 'form-control form-select'}),
                    'city': forms.Select(attrs={'class': 'form-control form-select'}),
        }