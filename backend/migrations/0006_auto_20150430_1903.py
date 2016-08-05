# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_auto_20150430_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='analiseporperiodo',
            name='periodoTempo',
            field=models.ForeignKey(default=1, to='backend.Periodo'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='analise',
            name='periodo',
            field=models.DateField(default=datetime.datetime(2015, 4, 30, 19, 3, 25, 901190)),
        ),
        migrations.AlterField(
            model_name='analiseporperiodo',
            name='periodo',
            field=models.DateField(default=datetime.datetime(2015, 4, 30, 19, 3, 25, 902937)),
        ),
        migrations.AlterField(
            model_name='periodo',
            name='data',
            field=models.DateField(default=datetime.datetime(2015, 4, 30, 19, 3, 25, 898927)),
        ),
        migrations.AlterField(
            model_name='ponto',
            name='periodo',
            field=models.DateField(default=datetime.datetime(2015, 4, 30, 19, 3, 25, 899670)),
        ),
    ]
