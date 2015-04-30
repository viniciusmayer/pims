# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_auto_20150430_1917'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='analiseporperiodo',
            options={'ordering': ['-ativo', '-periodo__data', '-data_hora_atualizacao', '-data_hora_criacao'], 'verbose_name_plural': 'analises por periodo'},
        ),
        migrations.RenameField(
            model_name='analiseporperiodo',
            old_name='periodoTempo',
            new_name='periodo',
        ),
        migrations.AlterField(
            model_name='analise',
            name='periodo',
            field=models.DateField(default=datetime.datetime(2015, 4, 30, 19, 17, 53, 167387)),
        ),
        migrations.AlterField(
            model_name='periodo',
            name='data',
            field=models.DateField(default=datetime.datetime(2015, 4, 30, 19, 17, 53, 164987)),
        ),
        migrations.AlterField(
            model_name='ponto',
            name='periodo',
            field=models.DateField(default=datetime.datetime(2015, 4, 30, 19, 17, 53, 165759)),
        ),
    ]
