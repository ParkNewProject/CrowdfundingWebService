import datetime

from django import forms
from django.contrib.auth.forms import UserCreationForm
from crowdfunding.models import CrfProject, CrfUser, Contribute


# Create your models here.

class RegisterForm(UserCreationForm):
    user_id = forms.CharField(
        label='아이디',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '아이디',
            }
        )
    )
    user_name = forms.CharField(
        label='이름',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '이름',
            }
        )
    )
    email = forms.EmailField(
        label='이메일',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': '이메일',
            }
        )
    )
    password1 = forms.CharField(
        label='비밀번호',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '비밀번호',
            }
        )
    )
    password2 = forms.CharField(
        label='비밀번호 확인',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '비밀번호 확인',
            }
        )
    )

    class Meta:
        model = CrfUser
        fields = ('user_id', 'user_name', 'email')

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
        label='아이디',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '아이디',
            }
        )
    )
    password = forms.CharField(
        label='비밀번호',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '비밀번호',
            }
        )
    )


class NewProjectForm(forms.ModelForm):
    # fin_time = forms.DateField(
    #     widget=forms.SelectDateWidget(),
    #     initial=datetime.date.today(),
    # )

    class Meta:
        model = CrfProject
        fields = ['pType', 'pImage', 'pTitle', 'pIntro', 'pContext', 'goalcoin', ]


class ContributeForm(forms.ModelForm):
    class Meta:
        model = Contribute
        fields = ['contrib_coin', ]


class EditForm(forms.ModelForm):

    class Meta:
        model = CrfUser
        fields = ('user_id', 'user_name', 'email')