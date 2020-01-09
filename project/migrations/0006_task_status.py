# Generated by Django 3.0.1 on 2020-01-09 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_report'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(blank=True, choices=[('0', 'активна'), ('1', 'завершена')], default='0', max_length=5, null=True, verbose_name='Статус'),
        ),
    ]
