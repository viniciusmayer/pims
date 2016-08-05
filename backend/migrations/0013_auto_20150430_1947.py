# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0012_auto_20150430_1938'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movimento',
            options={'ordering': ['-ativo', '-ponto__periodoTempo__data', '-data_hora_atualizacao', '-data_hora_criacao']},
        ),
        migrations.AlterModelOptions(
            name='ponto',
            options={'ordering': ['-ativo', '-periodoTempo__data', '-data_hora_atualizacao', '-data_hora_criacao']},
        ),
        migrations.RemoveField(
            model_name='ponto',
            name='periodo',
        ),
        migrations.AlterField(
            model_name='periodo',
            name='data',
            field=models.DateField(default=datetime.datetime(2015, 4, 30, 19, 47, 15, 186466)),
        ),
    ]
