# Generated by Django 4.1 on 2022-09-01 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0004_rename_habilidades_habilidad_empleado_habilidades'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='habilidad',
            options={'verbose_name': 'Habilidad', 'verbose_name_plural': 'Habilidades'},
        ),
    ]