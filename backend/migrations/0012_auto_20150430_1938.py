# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0011_auto_20150430_1931'),
    ]

    operations = [
        migrations.AddField(
            model_name='ponto',
            name='periodoTempo',
            field=models.ForeignKey(default=1, to='backend.Periodo'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='periodo',
            name='data',
            field=models.DateField(default=datetime.datetime(2015, 4, 30, 19, 38, 15, 907231)),
        ),
        migrations.AlterField(
            model_name='ponto',
            name='periodo',
            field=models.DateField(default=datetime.datetime(2015, 4, 30, 19, 38, 15, 908033)),
        ),
    ]
