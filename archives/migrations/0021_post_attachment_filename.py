# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-02 13:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archives', '0020_auto_20161025_0229'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='attachment_filename',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='附件文件名'),
        ),
    ]
