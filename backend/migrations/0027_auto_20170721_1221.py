# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-21 15:21
from __future__ import unicode_literals

from django.db import migrations, models

def setQuandoFromPonto(apps, schema_editor):
    movimentos = apps.get_model('backend', 'movimento')
    for movimento in movimentos.objects.all().iterator():
        movimento.quando = movimento.ponto.quando
        movimento.save()

class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0026_rendimentoporperiodo_quando'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='periodo',
            name='periodoAnterior',
        ),
        migrations.RemoveField(
            model_name='periodo',
            name='usuario_atualizacao',
        ),
        migrations.RemoveField(
            model_name='periodo',
            name='usuario_criacao',
        ),
        migrations.AlterModelOptions(
            name='rendimentoporperiodo',
            options={'ordering': ['-ativo', '-quando', '-data_hora_atualizacao', '-data_hora_criacao'], 'verbose_name_plural': 'rendimentos por periodo'},
        ),
        migrations.RemoveField(
            model_name='rendimentoporperiodo',
            name='periodo',
        ),
        migrations.AddField(
            model_name='movimento',
            name='quando',
            field=models.DateField(null=True),
        ),
        migrations.RunPython(setQuandoFromPonto),
        migrations.AlterField(
            model_name='movimento',
            name='quando',
            field=models.DateField(),
        ),
        migrations.DeleteModel(
            name='Periodo',
        ),
    ]