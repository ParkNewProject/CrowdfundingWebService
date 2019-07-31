from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('showProjects', views.showprojects, name='showProjects'),
    path('introProject', views.introproject, name='introProject'),

    path('registerLogin', views.registerlogin, name='registerLogin'),
    path('changePassword', views.changepassword, name='changePassword'),

    path('userProfile', views.userprofile, name='userProfile'),
    path('userProjects', views.userprojects, name='userProjects'),
]