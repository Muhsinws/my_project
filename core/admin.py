from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *


class UserAdmin(BaseUserAdmin):
    model = CustomUser

    list_display = ('id', 'email', 'is_active', 'is_staff', 'is_superuser',)

    
    ordering = ('-id',)

admin.site.register(CustomUser, UserAdmin)