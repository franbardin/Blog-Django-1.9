# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-29 14:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20160729_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagen',
            field=models.ImageField(default='blog/static/css/imagenes/242.png', upload_to='blog/static/subidas/img'),
        ),
    ]
