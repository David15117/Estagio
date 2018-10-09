# Generated by Django 2.1 on 2018-10-09 22:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('coordenador', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LinhaDotempo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arquivo', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('orientador', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='coordenador.Orientador')),
                ('orientando', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='coordenador.Orientando')),
            ],
            options={
                'verbose_name': 'Linha Do tempo',
                'verbose_name_plural': 'Linhas Do tempo',
            },
        ),
    ]
