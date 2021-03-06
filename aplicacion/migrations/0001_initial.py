# Generated by Django 4.0.4 on 2022-04-23 00:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
                ('email', models.EmailField(max_length=254, verbose_name='Correo electrónico')),
                ('telefono', models.CharField(max_length=10)),
                ('direccion', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateField(default=datetime.datetime)),
            ],
        ),
    ]
