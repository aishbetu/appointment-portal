from django import forms
from django.forms import fields
from .models import Covid_Test_Model

class Covid_Test_Form(forms.ModelForm):
    class Meta:
        model = Covid_Test_Model
        fields = ["name", "age", "gender", "phone", "email", "adhaar_no", "address", "date", "Time"]

        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control'}),
            "age": forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
            "gender": forms.Select(attrs={'class': 'form-control'}),
            "phone": forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
            "email": forms.TextInput(attrs={'class': 'form-control'}),
            "adhaar_no": forms.TextInput(attrs={'class': 'form-control'}),
            "address": forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            "date": forms.TextInput(attrs={'class': 'form-control'}),
            "Time": forms.TextInput(attrs={'class': 'form-control'}),
        }