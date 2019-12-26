from django.contrib import admin
from .models import Profile, Organisation, Task, Project
# Register your models here.

@admin.register(Organisation)
class OrganisationAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user']

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['project', 'priority', 'name', 'data_send', 'time', 'report', 'organisation']

@admin.register(Project)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'time']