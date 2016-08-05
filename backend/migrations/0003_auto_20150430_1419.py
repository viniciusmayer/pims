# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20150430_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analise',
            name='periodo',
            field=models.DateField(default=datetime.datetime(2015, 4, 30, 14, 19, 29, 402334)),
        ),
        migrations.AlterField(
            model_name='analiseporperiodo',
            name='periodo',
            field=models.DateField(default=datetime.datetime(2015, 4, 30, 14, 19, 29, 404958)),
        ),
        migrations.AlterField(
            model_name='periodo',
            name='data',
            field=models.DateField(default=datetime.datetime(2015, 4, 30, 14, 19, 29, 398854)),
        ),
        migrations.AlterField(
            model_name='ponto',
            name='periodo',
            field=models.DateField(default=datetime.datetime(2015, 4, 30, 14, 19, 29, 400032)),
        ),
        migrations.AlterField(
            model_name='rendimentoporperiodo',
            name='periodo',
            field=models.DateField(default=datetime.datetime(2015, 4, 30, 14, 19, 29, 406927)),
        ),
    ]
