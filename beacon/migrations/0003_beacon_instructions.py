# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-05 08:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beacon', '0002_beacon_trace'),
    ]

    operations = [
        migrations.AddField(
            model_name='beacon',
            name='instructions',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]