# Generated by Django 3.2.3 on 2021-10-19 19:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='education',
            old_name='university',
            new_name='institute',
        ),
        migrations.RenameField(
            model_name='education',
            old_name='degree',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='education',
            name='example',
        ),
        migrations.RemoveField(
            model_name='education',
            name='summary',
        ),
        migrations.RemoveField(
            model_name='experience',
            name='summary',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='description',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='summary',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='example',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='icon',
        ),
        migrations.AlterField(
            model_name='link',
            name='user',
            field=models.ForeignKey(help_text='User links', on_delete=django.db.models.deletion.CASCADE, related_name='links', to=settings.AUTH_USER_MODEL),
        ),
    ]