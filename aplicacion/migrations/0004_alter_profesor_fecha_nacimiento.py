# Generated by Django 4.0.4 on 2022-04-23 00:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0003_remove_profesor_direccion_remove_profesor_telefono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profesor',
            name='fecha_nacimiento',
            field=models.DateField(verbose_name=datetime.date(2022, 4, 22)),
        ),
    ]
