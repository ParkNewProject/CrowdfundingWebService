from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from crowdfunding.models import CrfProject, Contribute, CrfUser
from .forms import LoginForm, NewProjectForm, RegisterForm, ContributeForm, EditForm
from django.contrib.auth import (
    authenticate,
    login as django_login,
    logout as django_logout)
from django.urls import reverse

import logging
logger = logging.getLogger(__name__)

types = (
    ('G', '게임'),
    ('A', '예술'),
    ('F', '패션'),
    ('C', '캠페인'),
)


# 메인 화면
def index(request):
    projects = CrfProject.objects.all().order_by('cre_time')
    return render(request, 'crowdfunding/index.html', {
        'types': types,
        'projects': projects,
    })


# 프로젝트 조회 화면
def showprojects(request):
    projects = CrfProject.objects.all().order_by('cre_time')
    qproject = projects
    q = request.GET.get('q', '')  # q 내용 또는 빈 문자열
    if q:
        qproject = projects.filter(pTitle__icontains=q).order_by('cre_time')  # 제목에 q 포함 필터링

    return render(request, 'crowdfunding/showProjects.html', {
        'types': types,
        'projects': qproject,
        'q': q,
    })


# 개별 조회
def detail(request, projectid):
    projects = CrfProject.objects.all().order_by('cre_time')
    # 아이디로 조회된 프로젝트
    if projectid:
        logger.info('projectid is ' + projectid)
        i_projects = projects.filter(pid=projectid)
        t_projects = projects.filter(pType=i_projects[0].pType)     # 타입(종류)가 같은 추천 프로젝트
        return render(request, 'crowdfunding/detail.html', {
            'projectid': projectid,
            'types': types,
            'i_projects': i_projects,
            't_projects': t_projects,
        })

    else:
        return render(request, 'crowdfunding/index.html', {
        'types': types,
        'projects': projects,
    })


# 프로젝트 아이디 계산 함수
def project_id():
    from random import choice
    import string
    arr = [choice(string.ascii_letters) for _ in range(8)]
    pid = ''.join(arr)
    return pid

# 새 프로젝트 등록
@login_required
def newproject(request):
    if request.method == "POST":
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.pid = project_id()
            post.pType = request.POST['pType']
            post.pImage = request.FILES['pImage']
            post.pTitle = request.POST['pTitle']
            post.pIntro = request.POST['pIntro']
            post.pContext = request.POST['pContext']
            post.goalcoin = request.POST['goalcoin']

            post.owned_user = request.user
            post.save()
            return redirect('/detail/' + str(post.pid))
    else:
        form = NewProjectForm()
    return render(request, 'crowdfunding/newProject.html', {'form': form})

@login_required
def contribute(request, projectid):
    contrib_proj = CrfProject.objects.get(pid=projectid)
    user_self = CrfUser.objects.get(user_id=request.user.user_id)

    projects = CrfProject.objects.all().order_by('cre_time')
    i_projects = projects.filter(pid=projectid)
    t_projects = projects.filter(pType=i_projects[0].pType)  # 타입(종류)가 같은 추천 프로젝트

    if request.method == "POST":
        form = ContributeForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)

            post.contrib_pid = contrib_proj
            post.contrib_user = request.user
            post.contrib_coin = form.cleaned_data['contrib_coin']

            if request.user.usercoin > post.contrib_coin:

                #후원 코인 계산
                request.user.usercoin = request.user.usercoin - post.contrib_coin
                contrib_proj.nowcoin = contrib_proj.nowcoin + post.contrib_coin

                post.save()
                contrib_proj.save()
                request.user.save()
                return redirect('/detail/'+projectid)
            else:
                return render(request, 'crowdfunding/detail.html', {
                    'user_self': user_self,
                    'form': form,
                    'projectid': projectid,
                    'types': types,
                    'i_projects': i_projects,
                    't_projects': t_projects,
                })
    else:
        form = ContributeForm()
        return render(request, 'crowdfunding/contribute.html', {

                    'user_self': user_self,
                    'form': form,
                    'projectid': projectid,
                    'types': types,
                    'i_projects': i_projects,
                    't_projects': t_projects,
                })

@login_required
def edit(request, projectid):
    logger.info('projectid is ' + projectid)
    #수정할 프로젝트 객체 가져오기
    edit_proj = CrfProject.objects.get(pid=projectid)

    if request.method == "POST":
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            edit_proj.pType = request.POST['pType']
            edit_proj.pImage = request.FILES['pImage']
            edit_proj.pTitle = request.POST['pTitle']
            edit_proj.pIntro = request.POST['pIntro']
            edit_proj.pContext = request.POST['pContext']
            edit_proj.goalcoin = request.POST['goalcoin']

            edit_proj.owned_user = request.user
            edit_proj.save()
            return redirect('/detail/' + str(projectid))

    else:
        form = NewProjectForm(instance=edit_proj)
        context = {
            'form': form,
            'projectid': projectid,
        }
        return render(request, 'crowdfunding/edit.html', context)

@login_required
def delete(request, projectid):
    #삭제할 프로젝트 객체 가져오기
    delete_proj = CrfProject.objects.get(pid=projectid)
    delete_proj.delete()
    return redirect('/showProjects')

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

@login_required
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

@login_required
def userprofile(request):

    user_self = CrfUser.objects.get(user_id=request.user.user_id)

    if user_self:
        logger.info(str(user_self.user_id)+'!!!!!!!!!!!!!!')
    else:
        logger.info('???????????')

    if request.method == 'POST':
        form = EditForm(request.POST)
        if form.is_valid():
            user_self.user_id = request.POST['user_id']
            user_self.user_name = request.FILES['user_name']
            user_self.email = request.POST['email']
            user_self.save()

            return redirect(reverse('userProfile'))
    else:
        form = EditForm(instance=user_self)

    context = {
        'form': form,
        'user_self': user_self,
    }
    return render(request, 'crowdfunding/userProfile.html', context)


@login_required
def userprojects(request):
    projects = CrfProject.objects.all().order_by('cre_time')
    u_project = projects.filter(owned_user=request.user).order_by('cre_time')
    return render(request, 'crowdfunding/userProjects.html', {'types': types, 'u_project': u_project})

#에러
@login_required
def contribprojects(request):
    projects = CrfProject.objects.all().order_by('cre_time')
    c_project = []
    con = Contribute.objects.filter(contrib_user=request.user)
    for c in con:
        logger.info(str(c.contrib_pid) + '!!!!!!!!!!!!!!')
        c_project += projects.filter(pid=c.contrib_pid)
    return render(request, 'crowdfunding/contribProjects.html', {'types': types, 'c_project': c_project})


def charge(request):
    user_self = CrfUser.objects.get(user_id=request.user.user_id)
    user_self.usercoin = user_self.usercoin+50000
    user_self.save()

    form = EditForm(instance=user_self)
    context = {

        'form': form,
        'user_self': user_self,
    }
    return render(request, 'crowdfunding/userProfile.html', context)