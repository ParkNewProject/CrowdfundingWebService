from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('showProjects', views.showprojects, name='showProjects'),
    path('detail/<str:projectid>/', views.detail, name="detail"),

    # ex: /introProject/BdJgZDVt
    path('newProject', views.newproject, name='newProject'),
    path('contribute/<str:projectid>/', views.contribute, name='contribute'),

    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),

    path('userProfile', views.userprofile, name='userProfile'),
    path('userProjects', views.userprojects, name='userProjects'),
]