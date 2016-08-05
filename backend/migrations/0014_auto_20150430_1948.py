# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0013_auto_20150430_1947'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movimento',
            options={'ordering': ['-ativo', '-ponto__periodo__data', '-data_hora_atualizacao', '-data_hora_criacao']},
        ),
        migrations.AlterModelOptions(
            name='ponto',
            options={'ordering': ['-ativo', '-periodo__data', '-data_hora_atualizacao', '-data_hora_criacao']},
        ),
        migrations.RenameField(
            model_name='ponto',
            old_name='periodoTempo',
            new_name='periodo',
        ),
        migrations.AlterField(
            model_name='periodo',
            name='data',
            field=models.DateField(default=datetime.datetime(2015, 4, 30, 19, 48, 1, 504691)),
        ),
    ]
