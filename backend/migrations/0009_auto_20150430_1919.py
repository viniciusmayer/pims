# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_auto_20150430_1917'),
    ]

    operations = [
        migrations.AddField(
            model_name='analise',
            name='periodoTempo',
            field=models.ForeignKey(to='backend.Periodo', default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='analise',
            name='periodo',
            field=models.DateField(default=datetime.datetime(2015, 4, 30, 19, 19, 11, 370550)),
        ),
        migrations.AlterField(
            model_name='periodo',
            name='data',
            field=models.DateField(default=datetime.datetime(2015, 4, 30, 19, 19, 11, 368161)),
        ),
        migrations.AlterField(
            model_name='ponto',
            name='periodo',
            field=models.DateField(default=datetime.datetime(2015, 4, 30, 19, 19, 11, 368940)),
        ),
    ]
