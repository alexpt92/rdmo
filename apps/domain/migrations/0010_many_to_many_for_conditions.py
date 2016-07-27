# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-26 15:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conditions', '0002_many_to_many_for_conditions'),
        ('domain', '0009_remove_condition'),
    ]

    operations = [
        migrations.AddField(
            model_name='attributeentity',
            name='conditions',
            field=models.ManyToManyField(to='conditions.Condition'),
        ),
    ]
