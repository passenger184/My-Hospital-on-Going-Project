from .models import Patient
from django.forms import ModelForm
from django import forms

class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'