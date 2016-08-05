# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.db import models, migrations
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0015_auto_20150513_2057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tipo',
            name='categoria',
        ),
        migrations.AlterField(
            model_name='periodo',
            name='data',
            field=models.DateField(default=datetime.datetime(2015, 5, 14, 0, 0, 47, 643982, tzinfo=utc)),
        ),
    ]
