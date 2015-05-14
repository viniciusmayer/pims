# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0014_auto_20150430_1948'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='local',
            name='tipo',
        ),
        migrations.AlterField(
            model_name='periodo',
            name='data',
            field=models.DateField(default=datetime.datetime(2015, 5, 13, 23, 57, 59, 808488, tzinfo=utc)),
        ),
    ]
