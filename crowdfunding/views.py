from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import (
    authenticate,
    login as django_login,
    logout as django_logout,
)
from django.urls import reverse

def index(request):
    return render(request, 'crowdfunding/index.html')


def showprojects(request):
    return render(request, 'crowdfunding/showProjects.html')


def introproject(request):
    return render(request, 'crowdfunding/introProject.html')

def newproject(request):
    return render(request, 'crowdfunding/newProject.html')


def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(
                username=username,
                password=password
            )
            if user:
                django_login(request, user)
                return redirect(reverse('index'))
            login_form.add_error(None, '아이디 또는 비밀번호가 올바르지 않습니다')
    else:
        login_form = LoginForm()
    context = {
        'login_form': login_form,
    }
    return render(request, 'crowdfunding/login.html', context)

def logout(request):
    django_logout(request)
    return redirect(reverse('index'))

def register(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            register_form.register()

            return redirect(reverse('login'))
    else:
        register_form = RegisterForm()

    context = {
        'register_form': register_form,
    }
    return render(request, 'crowdfunding/register.html', context)

def userprofile(request):
    return render(request, 'crowdfunding/userProfile.html')

def userprojects(request):
    return render(request, 'crowdfunding/userProjects.html')
