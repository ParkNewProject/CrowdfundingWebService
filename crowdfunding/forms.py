import datetime

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, ReadOnlyPasswordHashField
from crowdfunding.models import CrfProject, CrfUser

# Create your models here.

class RegisterForm(UserCreationForm):
    user_id = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '아이디',
                'label': '아이디',
            }
        )
    )
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '이름',
                'label': '이름',
            }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': '이메일',
                'label': '이메일',
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '비밀번호',
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '비밀번호 확인',
            }
        )
    )

    class Meta:
        model = CrfUser
        fields = ('user_id', 'username', 'email')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Password don`t match')

        return password2

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    user_id = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '아이디',
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '비밀번호',
            }
        )
    )

class ChangeForm(UserChangeForm):
    user_id = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '아이디',
            }
        )
    )
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '이름',
            }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': '이메일',
            }
        )
    )

    password = ReadOnlyPasswordHashField(label="비밀번호")

    class Meta:
        model = CrfUser
        fields = ('user_id', 'username',  'email')


class NewProjectForm(forms.ModelForm):
    # fin_time = forms.DateField(
    #     widget=forms.SelectDateWidget(),
    #     initial=datetime.date.today(),
    # )

    class Meta:
        model = CrfProject
        fields = ['pType', 'pImage', 'pTitle', 'pIntro', 'pContext', ]
