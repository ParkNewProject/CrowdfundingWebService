from django.shortcuts import render
from .forms import RegisterForm


def index(request):
    return render(request, 'crowdfunding/index.html')


def showprojects(request):
    return render(request, 'crowdfunding/showProjects.html')


def introproject(request):
    return render(request, 'crowdfunding/introProject.html')


def registerlogin(request):
    form = RegisterForm()
    return render(request, 'crowdfunding/registerLogin.html', {'form': form})


def changepassword(request):
    return render(request, 'crowdfunding/changePassword.html')


def userprofile(request):
    return render(request, 'crowdfunding/userProfile.html')


def userprojects(request):
    return render(request, 'crowdfunding/userProjects.html')
