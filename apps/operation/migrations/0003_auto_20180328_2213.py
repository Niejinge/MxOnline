# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-28 22:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0002_auto_20180315_2305'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coursecomments',
            old_name='comment',
            new_name='comments',
        ),
    ]