# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userAccount', '0002_auto_20160516_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='name',
            field=models.CharField(default='Account', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='account',
            name='description',
            field=models.CharField(max_length=200),
        ),
    ]
