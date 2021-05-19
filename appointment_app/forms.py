from django import forms
from .models import AppointmentModel

class AppoAppointmentForm(forms.ModelForm):
    class Meta:
        model = AppointmentModel
        fields = ["name", "age", "gender", "phone", "email", "address", "date", "Time", "Doctor", "disease_description"]

        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control'}),
            "age": forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
            "gender": forms.TextInput(attrs={'class': 'form-control'}),
            "phone": forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
            "email": forms.TextInput(attrs={'class': 'form-control'}),
            "address": forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            "date": forms.TextInput(attrs={'class': 'form-control'}),
            "Time": forms.TextInput(attrs={'class': 'form-control'}),
            "Doctor": forms.Select(attrs={'class': 'form-control'}),
            "disease_description": forms.Textarea(attrs={'class': 'form-control','rows': 2}),
        }