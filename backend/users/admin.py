from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.

from . import models
from . import forms


class CustomUserAdmin(UserAdmin):
    add_form = forms.CustomUserCreationForm
    form = forms.CustomUserChangeForm
    list_display = ['email', 'username', 'first_name', 'last_name', 'timezone', ]
    model = models.SiteUser


admin.site.register(models.SiteUser, CustomUserAdmin)
admin.site.register(models.Blockage)
