from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from .choices import *


# Create your models here.


class CrfUserManager(BaseUserManager):
    def create_user(self, user_id, username, email, password):
        if not user_id:
            raise ValueError('ID Required!')

        user = self.model(
            user_id=user_id,
            username=username,
            email=email,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_id, password):
        user = self.create_user(
            user_id=user_id,
            username='username',
            email='park@email.com',
            password=password,
        )

        user.is_superuser = True

        user.save(using=self._db)
        return user


class CrfUser(AbstractBaseUser, PermissionsMixin):
    user_id = models.CharField(max_length=16, unique=True, verbose_name='아이디')
    username = models.CharField(max_length=30, verbose_name='유저 이름')
    email = models.EmailField(max_length=50, verbose_name='이메일')
    usercoin = models.IntegerField(default=0, verbose_name='유저 코인')

    # 유저가 가지고 있는 코인양

    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = []

    objects = CrfUserManager()

    def __str__(self):
        return self.username

    def get_user_id(self):
        return self.user_id

    def get_username(self):
        return self.username

    @property
    def is_staff(self):
        return self.is_superuser

class CrfProject(models.Model):
    pType = models.CharField(max_length=2, choices=TYPE, default='G', verbose_name='종류')
    pid = models.CharField(max_length=10, primary_key=True, verbose_name='고유번호')
    pTitle = models.CharField(max_length=30, verbose_name='제목')

    pImage = models.ImageField(null=True, default='cf/default', upload_to='cf/%Y%M%d', verbose_name='이미지')  #이미지 업로드 & 조회가 안됨
    pIntro = models.CharField(max_length=50, null=True, verbose_name='소개글')
    pContext = models.TextField(null=True, verbose_name='본문')

    fin_time = models.DateField(auto_now_add=True, verbose_name='마감일') #마감일 등록 안됨
    cre_time = models.DateField(auto_now_add=True, verbose_name='등록일')
    owned_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='소유주')
    #목표코인/ 현재 모금코인


class Contribute(models.Model):
    contrib_user = models.ForeignKey(CrfUser, on_delete=models.CASCADE, default=1, verbose_name='기여자')
    pid = models.ForeignKey(CrfProject, on_delete=models.CASCADE, null=True, verbose_name='고유번호')
    #모금한 코인
