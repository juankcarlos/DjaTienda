# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-26 02:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carrito', '0007_auto_20160524_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detallesventa',
            name='facturas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carrito.Factura'),
        ),
        migrations.AlterField(
            model_name='factura',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2016, 5, 26, 2, 5, 16, 641470)),
        ),
    ]
