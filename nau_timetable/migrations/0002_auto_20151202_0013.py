# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nau_timetable', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('full_name', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=140)),
                ('description', models.TextField()),
                ('date', models.DateTimeField()),
                ('type', models.IntegerField(choices=[(0, 'конференція'), (1, 'семінар'), (2, 'збори')])),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('date', models.DateTimeField()),
                ('type', models.IntegerField(choices=[(0, 'консультація'), (1, 'залік'), (2, 'іспит')])),
                ('groups', models.ManyToManyField(to='nau_timetable.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('full_name', models.CharField(max_length=140)),
                ('head', models.ForeignKey(to='nau_timetable.Teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('last_name', models.CharField(max_length=32)),
                ('first_name', models.CharField(max_length=32)),
                ('middle_name', models.CharField(max_length=32)),
                ('group', models.ForeignKey(to='nau_timetable.Group')),
            ],
        ),
        migrations.AddField(
            model_name='room',
            name='capacity',
            field=models.IntegerField(null=True, default=None),
        ),
        migrations.AddField(
            model_name='room',
            name='type',
            field=models.IntegerField(choices=[(0, 'лекційна аудиторія'), (1, 'звичайна аудиторія'), (2, 'лабораторія'), (3, 'мультимедійна аудиторія'), (99, 'актова зала')], default=1),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='type',
            field=models.IntegerField(null=True, choices=[(0, 'лекція'), (1, 'практика'), (2, 'лабораторна'), (3, 'консультація')]),
        ),
        migrations.AddField(
            model_name='exam',
            name='room',
            field=models.ForeignKey(to='nau_timetable.Room'),
        ),
        migrations.AddField(
            model_name='exam',
            name='subject',
            field=models.ForeignKey(to='nau_timetable.Subject'),
        ),
        migrations.AddField(
            model_name='exam',
            name='teacher',
            field=models.ForeignKey(to='nau_timetable.Teacher'),
        ),
        migrations.AddField(
            model_name='event',
            name='room',
            field=models.ForeignKey(to='nau_timetable.Room'),
        ),
        migrations.AddField(
            model_name='department',
            name='faculty',
            field=models.ForeignKey(to='nau_timetable.Faculty'),
        ),
        migrations.AddField(
            model_name='department',
            name='head',
            field=models.ForeignKey(to='nau_timetable.Teacher'),
        ),
        migrations.AddField(
            model_name='group',
            name='commander',
            field=models.ForeignKey(default=None, null=True, to='nau_timetable.Student', related_name='managed_group'),
        ),
        migrations.AddField(
            model_name='room',
            name='department',
            field=models.ForeignKey(default=None, null=True, to='nau_timetable.Department'),
        ),
    ]
