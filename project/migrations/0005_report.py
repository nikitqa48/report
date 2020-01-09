# Generated by Django 3.0.1 on 2020-01-09 11:49

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_remove_task_report'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Текст отчета')),
                ('data_send', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('report_task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Task')),
            ],
            options={
                'verbose_name': 'Отчет',
                'verbose_name_plural': 'Отчеты',
            },
        ),
    ]