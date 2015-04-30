# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20150430_1847'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rendimentoporperiodo',
            options={'verbose_name_plural': 'rendimentos por periodo', 'ordering': ['-ativo', '-periodo__data', '-data_hora_atualizacao', '-data_hora_criacao']},
        ),
        migrations.RenameField(
            model_name='rendimentoporperiodo',
            old_name='periodoTempo',
            new_name='periodo',
        ),
        migrations.AlterField(
            model_name='analise',
            name='periodo',
            field=models.DateField(default=datetime.datetime(2015, 4, 30, 18, 50, 45, 471796)),
        ),
        migrations.AlterField(
            model_name='analiseporperiodo',
            name='periodo',
            field=models.DateField(default=datetime.datetime(2015, 4, 30, 18, 50, 45, 473551)),
        ),
        migrations.AlterField(
            model_name='periodo',
            name='data',
            field=models.DateField(default=datetime.datetime(2015, 4, 30, 18, 50, 45, 469395)),
        ),
        migrations.AlterField(
            model_name='ponto',
            name='periodo',
            field=models.DateField(default=datetime.datetime(2015, 4, 30, 18, 50, 45, 470139)),
        ),
    ]
