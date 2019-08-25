from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from crowdfunding.forms import RegisterForm
from .models import CrfProject, CrfUser, Contribute

admin.site.register(CrfProject)
admin.site.register(CrfUser)
admin.site.register(Contribute)

class CrfUserAdmin(UserAdmin):
    add_form = RegisterForm
    add_fieldsets = (
        ('기본 정보', {'fields': ('user_id', 'password1', 'password2')}),
        ('추가 정보', {'fields': ('username', 'email')})
    )

    search_fields = ('user_id', 'username',)
    ordering = ('username',)
    filter_horizontal = ()
