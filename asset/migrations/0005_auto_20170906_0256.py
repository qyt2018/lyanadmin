# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-06 02:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0004_auto_20170906_0210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permission',
            name='argument_list',
            field=models.CharField(blank=True, help_text='\u591a\u4e2a\u53c2\u6570\u4e4b\u95f4\u7528\u82f1\u6587\u534a\u89d2\u9017\u53f7\u9694\u5f00', max_length=255, verbose_name='\u53c2\u6570\u5217\u8868'),
        ),
    ]