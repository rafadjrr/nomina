# Generated by Django 4.1 on 2022-09-01 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estatus', models.BooleanField(auto_created=True, default=False, editable=False, verbose_name='Estatus')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Nombre')),
                ('nick', models.CharField(blank=True, max_length=20, verbose_name='Apodo')),
            ],
            options={
                'verbose_name': 'Departamento',
                'verbose_name_plural': 'Departamentos',
            },
        ),
    ]
