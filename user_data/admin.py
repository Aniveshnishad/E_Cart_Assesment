
from django.contrib import admin
from .models import UserTable


# Register your models here.

class username(admin.ModelAdmin):
    list_display = ['id', 'email', 'firstName', 'lastName']


admin.site.register(UserTable, username)
