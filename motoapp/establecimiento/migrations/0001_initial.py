# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-28 20:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('nombre', models.CharField(max_length=75)),
            ],
        ),
        migrations.CreateModel(
            name='Distrito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('nombre', models.CharField(max_length=75)),
                ('ubigeo', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Establecimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=300, null=True, verbose_name='Establecimiento')),
                ('direccion', models.CharField(blank=True, max_length=500, null=True, verbose_name='Dirección')),
                ('referencia', models.CharField(blank=True, help_text='Avenida,Calle,Cuadra de referecia', max_length=500, null=True, verbose_name='Referencia')),
                ('tlf_1', models.CharField(blank=True, max_length=7, null=True, verbose_name='Teléfono Fijo')),
                ('tlf_2', models.CharField(blank=True, max_length=9, null=True, verbose_name='Teléfono Celular 1')),
                ('tlf_3', models.CharField(blank=True, max_length=9, null=True, verbose_name='Teléfono Celular 2')),
                ('correo', models.CharField(blank=True, max_length=200, null=True, verbose_name='Correo')),
                ('latitud', models.DecimalField(blank=True, decimal_places=7, max_digits=10, null=True, verbose_name='Latitud')),
                ('longitud', models.DecimalField(blank=True, decimal_places=7, max_digits=10, null=True, verbose_name='Longitud')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/establecimiento')),
                ('distrito', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='distritos', to='establecimiento.Distrito')),
            ],
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('nombre', models.CharField(max_length=75)),
                ('departamento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='provincias', to='establecimiento.Departamento')),
            ],
        ),
        migrations.AddField(
            model_name='distrito',
            name='provincia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='distritos', to='establecimiento.Provincia'),
        ),
    ]
