from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class CrfProject(models.Model):
    pType = models.IntegerField()
    pid = models.CharField(max_length=10, primary_key=True)
    pTitle = models.CharField(max_length=30)
    fin_time = models.DateField()
    cre_time = models.DateField()
    email = models.ForeignKey(User, models.DO_NOTHING, db_column='email')

class ProjectUser(models.Model):
    username = models.ForeignKey(User, models.DO_NOTHING, db_column='username')
    pid = models.ForeignKey(CrfProject, models.DO_NOTHING, db_column='pid')
