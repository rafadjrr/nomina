# Generated by Django 4.1 on 2022-09-16 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='prueba',
            options={'verbose_name': 'registros de pruebas', 'verbose_name_plural': 'pruebas'},
        ),
        migrations.AddField(
            model_name='prueba',
            name='cantidad',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]