# Generated by Django 4.2.7 on 2024-01-14 15:38

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_project_owner'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0002_proflie_username'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Proflie',
            new_name='Profile',
        ),
    ]