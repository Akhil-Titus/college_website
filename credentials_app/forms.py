from django import forms
from .models import Department, Course

class FormAppForm(forms.Form):
    name = forms.CharField(max_length=100)
    # Add other fields as required (DOB, AGE, GENDER, PHONE NUMBER, etc.)
    dob = forms.CharField(max_length=100)
    age = forms.CharField(max_length=100)
    gender = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=100)
    department = forms.ModelChoiceField(queryset=Department.objects.all())
    course = forms.ModelChoiceField(queryset=Course.objects.all())
    # course = forms.ModelChoiceField(queryset=Course.objects.none())
    # Add other fields as required (purpose, Materials provide, etc.)
