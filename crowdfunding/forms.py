from django import forms
from .models import CrfUser


class RegisterForm(forms.ModelForm):
    class Meta:
        model = CrfUser
        fields = ('email', 'username', 'password',)
