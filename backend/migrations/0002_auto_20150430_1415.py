# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rendimentoporperiodo',
            name='periodoTempo',
            field=models.ForeignKey(default=1, to='backend.Periodo'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='analise',
            name='periodo',
            field=models.DateField(default=datetime.datetime(2015, 4, 30, 14, 14, 34, 205565)),
        ),
        migrations.AlterField(
            model_name='analiseporperiodo',
            name='periodo',
            field=models.DateField(default=datetime.datetime(2015, 4, 30, 14, 14, 34, 207628)),
        ),
        migrations.AlterField(
            model_name='periodo',
            name='data',
            field=models.DateField(default=datetime.datetime(2015, 4, 30, 14, 14, 34, 203204)),
        ),
        migrations.AlterField(
            model_name='ponto',
            name='periodo',
            field=models.DateField(default=datetime.datetime(2015, 4, 30, 14, 14, 34, 203986)),
        ),
        migrations.AlterField(
            model_name='rendimentoporperiodo',
            name='periodo',
            field=models.DateField(default=datetime.datetime(2015, 4, 30, 14, 14, 34, 209051)),
        ),
    ]
