from django.contrib.auth import get_user_model
from django.db import models
from .choices import *
# Create your models here.

User = get_user_model()

class CrfProject(models.Model):
    pType = models.CharField(max_length=2, choices=TYPE, default='G')
    pid = models.CharField(max_length=10, primary_key=True)
    pTitle = models.CharField(max_length=30)
    pIntro = models.CharField(max_length=50, null=True)
    pContext = models.TextField(null=True)
    fin_time = models.DateField()
    cre_time = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class ProjectUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    pid = models.ForeignKey(CrfProject, on_delete=models.CASCADE, null=True)
