from .models import Teachers,Students
from django import forms


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teachers
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'profession',
            'fakultet',
            'data'
        )
        widgets={
            "first_name":forms.TextInput(attrs={'class':'form-control'}),
            "last_name": forms.TextInput(attrs={'class': 'form-control'}),
            "email": forms.EmailInput(attrs={'class': 'form-control'}),
            "profession": forms.Select(attrs={'class': 'form-control'}),
            "fakultet": forms.Select(attrs={'class': 'form-control'}),
            "data": forms.DateInput(attrs={'class': 'form-control'}),

        }

class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'profession',
            'fakultet',
            'data'
        )
        widgets={
            "first_name":forms.TextInput(attrs={'class':'form-control'}),
            "last_name": forms.TextInput(attrs={'class': 'form-control'}),
            "email": forms.EmailInput(attrs={'class': 'form-control'}),
            "profession": forms.Select(attrs={'class': 'form-control'}),
            "fakultet": forms.Select(attrs={'class': 'form-control'}),
            "data": forms.DateInput(attrs={'class': 'form-control'}),

        }
