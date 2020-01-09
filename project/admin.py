from django.contrib import admin
from .models import Profile, Organisation, Task, Project, Report
# Register your models here.

@admin.register(Organisation)
class OrganisationAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user']

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['project', 'priority', 'name', 'data_send', 'time', 'organisation','status']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'time']
    
@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ['data_send', 'description', 'report_task']
