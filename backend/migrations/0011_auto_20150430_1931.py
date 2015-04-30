# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0010_auto_20150430_1930'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='analise',
            options={'ordering': ['-ativo', '-periodo__data', '-data_hora_atualizacao', '-data_hora_criacao']},
        ),
        migrations.RenameField(
            model_name='analise',
            old_name='periodoTempo',
            new_name='periodo',
        ),
        migrations.AlterField(
            model_name='periodo',
            name='data',
            field=models.DateField(default=datetime.datetime(2015, 4, 30, 19, 31, 18, 884266)),
        ),
        migrations.AlterField(
            model_name='ponto',
            name='periodo',
            field=models.DateField(default=datetime.datetime(2015, 4, 30, 19, 31, 18, 885044)),
        ),
    ]
