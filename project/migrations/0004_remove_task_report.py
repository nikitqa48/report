# Generated by Django 3.0.1 on 2020-01-09 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20191226_1701'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='report',
        ),
    ]
