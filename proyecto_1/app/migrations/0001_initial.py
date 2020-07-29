# Generated by Django 2.2.14 on 2020-07-22 01:16

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=200)),
                ('mail', models.EmailField(max_length=254)),
                ('creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creacion')),
                ('modificacion', models.DateTimeField(auto_now=True, verbose_name='Fecha Modificacion')),
            ],
            options={
                'verbose_name': 'Contacto',
                'verbose_name_plural': 'Contactos',
                'ordering': ['-creacion'],
            },
        ),
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('fecha', models.DateTimeField(default=datetime.datetime(2020, 7, 21, 20, 16, 9, 837061))),
                ('creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creacion')),
                ('modificacion', models.DateTimeField(auto_now=True, verbose_name='Fecha Modificacion')),
                ('contacto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Contacto')),
            ],
            options={
                'verbose_name': 'Entrada',
                'verbose_name_plural': 'Entradas',
                'ordering': ['-creacion'],
            },
        ),
    ]