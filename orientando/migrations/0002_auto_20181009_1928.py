# Generated by Django 2.1 on 2018-10-09 22:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orientando', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tempo',
            name='arquivo',
        ),
        migrations.RemoveField(
            model_name='tempo',
            name='comentario',
        ),
    ]
