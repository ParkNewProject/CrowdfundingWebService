from django.db import models
# Create your models here.

class CrfProject(models.Model):
    GAME = 'G'
    ART = 'A'
    FASHION = 'F'
    CAMPAIGN = 'C'
    pType = [
        (GAME, '게임'),
        (ART, '예술'),
        (FASHION, '패션'),
        (CAMPAIGN, '캠페인'),
    ]
    pid = models.CharField(max_length=10, primary_key=True)
    pTitle = models.CharField(max_length=30)
    pIntro = models.CharField(max_length=50, null=True)
    pContext = models.TextField(null=True)
    fin_time = models.DateField()
    cre_time = models.DateField(auto_now_add=True)
    user = models.CharField(max_length=10, null=True)

class ProjectUser(models.Model):
    pid = models.ForeignKey(CrfProject, on_delete=models.CASCADE, null=True)
