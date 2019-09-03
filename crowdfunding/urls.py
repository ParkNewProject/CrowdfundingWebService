from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('showProjects', views.showprojects, name='showProjects'),
    path('detail/<str:projectid>/', views.detail, name="detail"),

    path('newProject', views.newproject, name='newProject'),
    path('detail/<str:projectid>/contribute/', views.contribute, name='contribute'),
    path('detail/<str:projectid>/edit/', views.edit, name='edit'),
    path('detail/<str:projectid>/delete/', views.delete, name='delete'),

    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),

    path('userProfile', views.userprofile, name='userProfile'),
    path('userProjects', views.userprojects, name='userProjects'),
    path('contribProjects', views.contribprojects, name='contribProjects'),
]