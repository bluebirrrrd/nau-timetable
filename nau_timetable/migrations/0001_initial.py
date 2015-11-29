# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=2)),
                ('latitude', models.DecimalField(max_digits=9, decimal_places=6)),
                ('longitude', models.DecimalField(max_digits=9, decimal_places=6)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=6)),
                ('degree', models.IntegerField(choices=[(0, 'бакалавр'), (1, 'спеціаліст'), (2, 'магістр')])),
                ('type', models.IntegerField(choices=[(0, 'денна'), (1, 'заочна')])),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('number', models.IntegerField(choices=[(1, '1 пара'), (2, '2 пара'), (3, '3 пара'), (4, '4 пара'), (5, '5 пара'), (6, '6 пара')])),
                ('day', models.IntegerField(choices=[(1, 'понеділок'), (2, 'вівторок'), (3, 'середа'), (4, 'четвер'), (5, "п'ятниця"), (6, 'субота')])),
                ('week', models.BooleanField()),
                ('type', models.IntegerField(null=True, choices=[(0, 'лекція'), (1, 'практика'), (2, 'лабораторна')])),
                ('subgroup_num', models.IntegerField(default=None, null=True, choices=[(1, '1 підгрупа'), (2, '2 підгрупа')])),
                ('groups', models.ManyToManyField(to='nau_timetable.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=5)),
                ('building', models.ForeignKey(to='nau_timetable.Building')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('short_name', models.CharField(max_length=50)),
                ('full_name', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('last_name', models.CharField(max_length=32)),
                ('first_name', models.CharField(max_length=32)),
                ('middle_name', models.CharField(max_length=32)),
                ('position', models.IntegerField(null=True, choices=[(0, 'аспірант'), (1, 'асистент'), (2, 'старший викладач'), (3, 'доцент'), (4, 'професор')])),
            ],
        ),
        migrations.AddField(
            model_name='lesson',
            name='room',
            field=models.ForeignKey(to='nau_timetable.Room'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='subject',
            field=models.ForeignKey(to='nau_timetable.Subject'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='teacher',
            field=models.ForeignKey(to='nau_timetable.Teacher'),
        ),
    ]
