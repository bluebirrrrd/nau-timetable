# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('nau_timetable', '0002_auto_20151202_0013'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2015, 12, 21, 22, 22, 44, 368514)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='room',
            name='type',
            field=models.IntegerField(default=1, choices=[(0, 'лекційна аудиторія'), (1, 'звичайна аудиторія'), (2, 'лабораторія'), (3, 'мультимедійна аудиторія'), (4, 'актова зала')]),
        ),
        migrations.AlterField(
            model_name='subject',
            name='short_name',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
