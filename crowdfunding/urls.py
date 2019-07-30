from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('showProjects', views.showProjects, name='showProjects'),
    path('introProject', views.introProject, name='introProject'),

    path('registerLogin', views.registerLogin, name='registerLogin'),
    path('changePassword', views.changePassword, name='changePassword'),

    path('userProfile', views.userProfile, name='userProfile'),
    path('userProjects', views.userProjects, name='userProjects'),
]