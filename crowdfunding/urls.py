from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('showProjects', views.showprojects, name='showProjects'),
    path('introProject/<str:projectid>', views.introproject, name="introProject"),

    # ex: /introProject/BdJgZDVt
    path('newProject', views.newproject, name='newProject'),

    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),

    path('userProfile', views.userprofile, name='userProfile'),
    path('userProjects', views.userprojects, name='userProjects'),
]