# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-28 01:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categorias',
            field=models.CharField(choices=[('0', 'Trabajos Practicos'), ('1', 'Ejemplo'), ('2', 'Otros')], default='0', max_length=6),
        ),
    ]