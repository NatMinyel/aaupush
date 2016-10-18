# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-26 12:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20160826_1459'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('section_number', models.IntegerField()),
                ('code', models.CharField(max_length=10)),
                ('course', models.ManyToManyField(to='main.Course')),
                ('studyfield', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.StudyField')),
            ],
        ),
        migrations.AddField(
            model_name='announcement',
            name='section',
            field=models.ManyToManyField(to='main.Section'),
        ),
        migrations.AddField(
            model_name='material',
            name='section',
            field=models.ManyToManyField(to='main.Section'),
        ),
    ]
