# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-04 15:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0003_protect_scheduleitems_from_deletion'),
    ]

    operations = [
        migrations.AlterOrderWithRespectTo(
            name='slot',
            order_with_respect_to=None,
        ),
    ]