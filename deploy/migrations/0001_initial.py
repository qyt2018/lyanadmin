# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-05 09:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audit_time', models.DateTimeField(auto_now_add=True, verbose_name='\u65f6\u95f4')),
                ('type', models.CharField(max_length=10, verbose_name='\u7c7b\u578b')),
                ('action', models.CharField(max_length=10, verbose_name='\u52a8\u4f5c')),
                ('action_ip', models.CharField(max_length=15, verbose_name='\u6267\u884cIP')),
                ('content', models.CharField(max_length=50, verbose_name='\u5185\u5bb9')),
            ],
            options={
                'verbose_name': '\u5ba1\u8ba1\u4fe1\u606f',
            },
        ),
    ]
