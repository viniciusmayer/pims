# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_auto_20150430_1419'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rendimentoporperiodo',
            options={'verbose_name_plural': 'rendimentos por periodo', 'ordering': ['-ativo', '-periodoTempo__data', '-data_hora_atualizacao', '-data_hora_criacao']},
        ),
        migrations.RemoveField(
            model_name='rendimentoporperiodo',
            name='periodo',
        ),
        migrations.AlterField(
            model_name='analise',
            name='periodo',
            field=models.DateField(default=datetime.datetime(2015, 4, 30, 18, 47, 23, 59522)),
        ),
        migrations.AlterField(
            model_name='analiseporperiodo',
            name='periodo',
            field=models.DateField(default=datetime.datetime(2015, 4, 30, 18, 47, 23, 61294)),
        ),
        migrations.AlterField(
            model_name='periodo',
            name='data',
            field=models.DateField(default=datetime.datetime(2015, 4, 30, 18, 47, 23, 57170)),
        ),
        migrations.AlterField(
            model_name='ponto',
            name='periodo',
            field=models.DateField(default=datetime.datetime(2015, 4, 30, 18, 47, 23, 57935)),
        ),
    ]
