from django import forms
from .models import RegisterForm


class UserForm(forms.ModelForm):
    class Meta:
        model = RegisterForm
        fields = '__all__'
