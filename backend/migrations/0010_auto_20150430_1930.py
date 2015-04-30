# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0009_auto_20150430_1919'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='analise',
            options={'ordering': ['-ativo', '-periodoTempo__data', '-data_hora_atualizacao', '-data_hora_criacao']},
        ),
        migrations.RemoveField(
            model_name='analise',
            name='periodo',
        ),
        migrations.AlterField(
            model_name='periodo',
            name='data',
            field=models.DateField(default=datetime.datetime(2015, 4, 30, 19, 30, 19, 919818)),
        ),
        migrations.AlterField(
            model_name='ponto',
            name='periodo',
            field=models.DateField(default=datetime.datetime(2015, 4, 30, 19, 30, 19, 920612)),
        ),
    ]
