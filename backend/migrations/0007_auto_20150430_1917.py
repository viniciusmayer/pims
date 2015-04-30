# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_auto_20150430_1903'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='analiseporperiodo',
            options={'verbose_name_plural': 'analises por periodo', 'ordering': ['-ativo', '-periodoTempo__data', '-data_hora_atualizacao', '-data_hora_criacao']},
        ),
        migrations.RemoveField(
            model_name='analiseporperiodo',
            name='periodo',
        ),
        migrations.AlterField(
            model_name='analise',
            name='periodo',
            field=models.DateField(default=datetime.datetime(2015, 4, 30, 19, 17, 4, 908442)),
        ),
        migrations.AlterField(
            model_name='periodo',
            name='data',
            field=models.DateField(default=datetime.datetime(2015, 4, 30, 19, 17, 4, 906037)),
        ),
        migrations.AlterField(
            model_name='ponto',
            name='periodo',
            field=models.DateField(default=datetime.datetime(2015, 4, 30, 19, 17, 4, 906854)),
        ),
    ]
