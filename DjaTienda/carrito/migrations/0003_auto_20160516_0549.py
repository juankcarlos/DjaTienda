# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-16 05:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carrito', '0002_detallesventa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detallesventa',
            name='facturas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carrito.Factura'),
        ),
    ]
