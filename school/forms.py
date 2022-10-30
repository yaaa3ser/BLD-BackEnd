from django import forms
from .models import *
from django.forms import ValidationError

def check_first_name(name):
    if not name[0].isupper():
        raise ValidationError("first char must be uppercase")


class StudentForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100, validators = [check_first_name])

    class Meta:
        model = Student
        fields = "__all__"
