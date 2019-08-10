from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from crowdfunding.forms import RegisterForm, ChangeForm


class CrfUserAdmin(UserAdmin):
    form = ChangeForm
    list_display = ('user_id', 'username', 'email', )
    list_filter = ('is_superuser', )
    fieldsets = (
        ('아이디', {'fields': ('user_id', 'password')}),
        ('개인 정보', {'fields': ('username', 'email')}),
        ('권한', {'fields': ('is_superuser',)}),
    )

    add_form = RegisterForm
    add_fieldsets = (
        ('기본 정보', {'fields': ('user_id', 'password1', 'password2')}),
        ('추가 정보', {'fields': ('username', 'email')})
    )

    search_fields = ('user_id', 'username',)
    ordering = ('username',)
    filter_horizontal = ()
