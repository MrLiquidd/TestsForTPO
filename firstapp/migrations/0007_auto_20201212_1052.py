# Generated by Django 2.2.17 on 2020-12-12 07:52

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('firstapp', '0006_auto_20201212_1051'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Feed',
            new_name='Feedback',
        ),
    ]