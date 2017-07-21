# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-21 02:09
from __future__ import unicode_literals

from django.db import migrations, models

def setQuandoFromPeriodo(apps, schema_editor):
    rendimentosporperiodo = apps.get_model('backend', 'rendimentoporperiodo')
    for rendimentoporperiodo in rendimentosporperiodo.objects.all().iterator():
        rendimentoporperiodo.quando = rendimentoporperiodo.periodo.data
        rendimentoporperiodo.save()

class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0025_auto_20170720_1328'),
    ]

    operations = [
        migrations.AddField(
            model_name='rendimentoporperiodo',
            name='quando',
            field=models.DateField(null=True),
        ),
        migrations.RunPython(setQuandoFromPeriodo),
        migrations.AlterField(
            model_name='rendimentoporperiodo',
            name='quando',
            field=models.DateField(),
        ),
    ]
