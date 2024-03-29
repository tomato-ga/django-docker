# Generated by Django 4.2.2 on 2023-06-09 06:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_project_todomodel_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='todomodel',
            name='duedate',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='todomodel',
            name='priority',
            field=models.CharField(choices=[('danger', 'high'), ('warning', 'normal'), ('primary', 'low')], default='danger', max_length=100),
            preserve_default=False,
        ),
    ]
