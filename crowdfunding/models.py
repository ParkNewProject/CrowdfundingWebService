from django.db import models

# Create your models here.


class CrfUser(models.Model):
    email = models.CharField(max_length=30, primary_key=True)
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=10)


class CrfProject(models.Model):
    pType = models.IntegerField()
    pid = models.CharField(max_length=10, primary_key=True)
    pTitle = models.CharField(max_length=30)
    fin_time = models.DateField()
    cre_time = models.DateField()
    email = models.ForeignKey(CrfUser, models.DO_NOTHING, db_column='email')

class ProjectUser(models.Model):
    email = models.ForeignKey(CrfUser, models.DO_NOTHING, db_column='email')
    pid = models.ForeignKey(CrfProject, models.DO_NOTHING, db_column='pid')
