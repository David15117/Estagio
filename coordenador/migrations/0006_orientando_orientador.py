# Generated by Django 2.1 on 2018-10-10 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coordenador', '0005_remove_orientando_orientador'),
    ]

    operations = [
        migrations.AddField(
            model_name='orientando',
            name='orientador',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='coordenador.Orientador'),
        ),
    ]