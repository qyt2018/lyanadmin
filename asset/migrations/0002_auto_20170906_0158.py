# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-06 01:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='admin',
        ),
        migrations.RemoveField(
            model_name='newassetapprovalzone',
            name='approved',
        ),
        migrations.RemoveField(
            model_name='newassetapprovalzone',
            name='approved_by',
        ),
        migrations.RemoveField(
            model_name='newassetapprovalzone',
            name='approved_date',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]