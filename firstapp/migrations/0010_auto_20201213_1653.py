# Generated by Django 2.2.17 on 2020-12-13 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0009_history'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.Client'),
        ),
    ]
