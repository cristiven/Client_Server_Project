# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-04 02:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sgc', '0003_social_auth_usersocialauth'),
    ]

    operations = [
        migrations.DeleteModel(
            name='social_auth_usersocialauth',
        ),
    ]
