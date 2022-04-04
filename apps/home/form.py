from .models import Teachers,Students, Schedule, GroupNum
from django import forms


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teachers
        fields = (
            'id',
            'first_name',
            'last_name',
            'photo',
            'email',
            'profession',
            'fakultet',
            'data'
        )
        widgets={
            "first_name":forms.TextInput(attrs={'class':'form-control'}),
            "last_name": forms.TextInput(attrs={'class': 'form-control'}),
            "email": forms.EmailInput(attrs={'class': 'form-control'}),
            "photo": forms.FileInput(attrs={'class': 'form-control'}),
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
            'photo',
            'profession',
            'fakultet',
            'data'
        )
        widgets={
            "first_name":forms.TextInput(attrs={'class':'form-control'}),
            "last_name": forms.TextInput(attrs={'class': 'form-control'}),
            "email": forms.EmailInput(attrs={'class': 'form-control'}),
            "photo": forms.FileInput(attrs={'class': 'form-control'}),
            "profession": forms.Select(attrs={'class': 'form-control'}),
            "fakultet": forms.Select(attrs={'class': 'form-control'}),
            "data": forms.DateInput(attrs={'class': 'form-control'}),

        }

class ScheduleForm(forms.ModelForm):
    class Meta:
        model=Schedule
        fields = (
            'group_num',
            'time',
            'day',
            'subjects',
        )
        widgets={
            "group_num": forms.Select(attrs={'class': 'form-control'}),
            "time": forms.Select(attrs={'class': 'form-control'}),
            "day": forms.Select(attrs={'class': 'form-control'}),
            "subjects": forms.Select(attrs={'class': 'form-control'}),

        }

class GroupNumForm(forms.ModelForm):
    class Meta:
        model=GroupNum
        fields = (
            "__all__"
        )
        widgets={
            "group_num": forms.TextInput(attrs={'class': 'form-control'}),
            "students": forms.Select(attrs={'class': 'form-control'}),
            "teachers": forms.Select(attrs={'class': 'form-control'}),
        }