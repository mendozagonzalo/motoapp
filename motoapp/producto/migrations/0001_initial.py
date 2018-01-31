# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-04 15:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import easy_thumbnails.fields
import motoclick.utils.mixins


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('establecimiento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', easy_thumbnails.fields.ThumbnailerImageField(upload_to='productos/images', verbose_name='Fotos del producto')),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Marca')),
                ('codigo', models.CharField(max_length=50, verbose_name='Codigo')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='images/marca', verbose_name='Imagen Marca')),
            ],
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=200, null=True, verbose_name='Modelo')),
                ('codigo', models.CharField(max_length=50, verbose_name='Codigo')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modelo_marcas', to='producto.Marca')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=300, null=True, verbose_name='Producto')),
                ('categoria', models.CharField(choices=[('A', 'ACCESORIO'), ('R', 'REPUESTO')], default='A', max_length=1)),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripción general')),
                ('tipo_moneda', models.CharField(blank=True, choices=[('usd', 'Dólares'), ('pen', 'Soles')], max_length=3, null=True, verbose_name='Tipo de Moneda')),
                ('precio_bruto', models.FloatField(verbose_name='Precio Bruto')),
                ('descuento', models.PositiveIntegerField(blank=True, help_text='15%,30%, etc', null=True, verbose_name='Descuento')),
                ('precio_final', models.FloatField(blank=True, null=True, verbose_name='Precio con descuento')),
                ('fecha_registro', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Registro')),
                ('imagen_principal', easy_thumbnails.fields.ThumbnailerImageField(null=True, upload_to='productos/images', verbose_name='Imagen principal del producto')),
                ('stock', models.PositiveIntegerField(default=1, verbose_name='Stock')),
                ('establecimientos', models.ManyToManyField(blank=True, related_name='productos', to='establecimiento.Establecimiento')),
                ('marca', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='producto_marcas', to='producto.Marca')),
                ('modelo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='producto_modelos', to='producto.Modelo')),
            ],
            bases=(motoclick.utils.mixins.UidMixin, models.Model),
        ),
        migrations.AddField(
            model_name='imagen',
            name='producto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='producto.Producto', verbose_name='Producto'),
        ),
    ]
