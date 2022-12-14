# Generated by Django 4.1 on 2022-09-01 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departamento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=60, verbose_name='nombres')),
                ('last_name', models.CharField(max_length=60, verbose_name='apellidos')),
                ('jobs', models.CharField(choices=[('0', 'ingeniero informatico'), ('1', 'ingeniero sistemas'), ('2', 'electronico')], max_length=1, verbose_name='trabajo')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departamento.departamento')),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
            },
        ),
    ]
