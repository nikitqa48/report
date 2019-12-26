from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Project(models.Model):
    name = models.CharField('Название проекта', max_length=30)
    time = models.DateField('срок исполения проекта', blank = True, null = True)
    description = models.TextField('Описание проекта', blank=True, null=True)    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  
    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"



class Organisation(models.Model):
    name = models.CharField('Название отдела', max_length=40)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Отдел"
        verbose_name_plural = "Отделы"

class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    PRIORITY_STATUS = (('0', 'низкий'),('1', 'средний'), ('2', 'высокий'))
    description = models.TextField('Описание Задачи', blank=True, null=True)
    name = models.CharField('Название задачи', max_length=30)
    STATUS_TASK = (('0', 'активна'),('1','неактивна'))
    data_send = models.DateTimeField(default=timezone.now, blank=False, null = True)
    time = models.DateField('срок исполения задачи', blank = True, null = True)
    priority = models.CharField('приоритет', choices=PRIORITY_STATUS, null=True , blank = True, default='0', max_length=5)
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    report = models.TextField('Отчет', blank=True, null=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"





