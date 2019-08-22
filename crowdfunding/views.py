from django.contrib import messages
from django.shortcuts import render, redirect

from crowdfunding.models import CrfProject
from .forms import LoginForm, NewProjectForm, RegisterForm
from django.contrib.auth import (
    authenticate,
    login as django_login,
    logout as django_logout)
from django.urls import reverse


types = (
    ('G', '게임'),
    ('A', '예술'),
    ('F', '패션'),
    ('C', '캠페인'),
)
projects = CrfProject.objects.all()

def index(request):
    return render(request, 'crowdfunding/index.html', {'projects': projects})


def showprojects(request):
    qprojects = projects
    q = request.GET.get('q', '')            # q 내용 또는 빈 문자열
    if q:
        qprojects = projects.filter(pTitle__icontains=q)      # 제목에 q 포함 필터링

    return render(request, 'crowdfunding/showProjects.html', {
        'projects': qprojects,
        'q': q,
    })

def introproject(request):
    return render(request, 'crowdfunding/introProject.html')

def project_id():
    from random import choice
    import string
    arr = [choice(string.ascii_letters) for _ in range(8)]
    pid = ''.join(arr)
    return pid

def newproject(request):
    if request.method == "POST":
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.pid = project_id()
            post.owned_user = request.user
            post.save()
            return redirect('index')
    else:
        form = NewProjectForm()
    return render(request, 'crowdfunding/newProject.html', {'form': form})


def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_id = login_form.cleaned_data['user_id']
            password = login_form.cleaned_data['password']
            user = authenticate(
                user_id=user_id,
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
            register_form.save()
            messages.info(request, '성공적으로 회원가입했습니다!')
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
    u_project = projects.filter(owned_user=request.user).order_by('cre_time')
    return render(request, 'crowdfunding/userProjects.html', {'types': types, 'u_project': u_project})
