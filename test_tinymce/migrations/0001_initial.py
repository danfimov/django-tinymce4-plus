# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-01 09:56
from __future__ import unicode_literals

from django.db import migrations, models

import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', tinymce.models.HTMLField(verbose_name='HTML Content')),
            ],
        ),
    ]
