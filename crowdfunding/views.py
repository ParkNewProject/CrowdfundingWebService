from django.shortcuts import render

def index(request):
    return render(request, 'crowdfunding/index.html')

def showProjects(request):
    return render(request, 'crowdfunding/showProjects.html')

def introProject(request):
    return render(request, 'crowdfunding/introProject.html')


def registerLogin(request):
    return render(request, 'crowdfunding/registerLogin.html')

def changePassword(request):
    return render(request, 'crowdfunding/changePassword.html')


def userProfile(request):
    return render(request, 'crowdfunding/userProfile.html')

def userProjects(request):
    return render(request, 'crowdfunding/userProjects.html')