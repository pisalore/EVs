from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import EvUser


class CustomUserAdmin(UserAdmin):
    model = EvUser
    list_display = ['username', 'first_name', 'last_name', 'email', 'city', 'is_organizer']


admin.site.register(EvUser, CustomUserAdmin)
