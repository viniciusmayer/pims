# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.db.models.deletion
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Analise',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('observacoes', models.CharField(max_length=255, blank=True, null=True)),
                ('ativo', models.BooleanField(default=True)),
                ('excluido', models.BooleanField(default=False)),
                ('data_hora_criacao', models.DateTimeField(auto_now_add=True)),
                ('data_hora_atualizacao', models.DateTimeField(auto_now=True)),
                ('periodo', models.DateField(default=datetime.datetime(2015, 4, 30, 13, 42, 48, 103258))),
                ('analiseAnterior', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.Analise', blank=True)),
                ('usuario_atualizacao', models.ForeignKey(related_name='backend_analise_atualizacao_related', to=settings.AUTH_USER_MODEL, editable=False)),
                ('usuario_criacao', models.ForeignKey(related_name='backend_analise_criacao_related', to=settings.AUTH_USER_MODEL, editable=False)),
            ],
            options={
                'ordering': ['-ativo', '-periodo', '-data_hora_atualizacao', '-data_hora_criacao'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AnalisePorPeriodo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('observacoes', models.CharField(max_length=255, blank=True, null=True)),
                ('ativo', models.BooleanField(default=True)),
                ('excluido', models.BooleanField(default=False)),
                ('data_hora_criacao', models.DateTimeField(auto_now_add=True)),
                ('data_hora_atualizacao', models.DateTimeField(auto_now=True)),
                ('periodo', models.DateField(default=datetime.datetime(2015, 4, 30, 13, 42, 48, 104378))),
                ('usuario_atualizacao', models.ForeignKey(related_name='backend_analiseporperiodo_atualizacao_related', to=settings.AUTH_USER_MODEL, editable=False)),
                ('usuario_criacao', models.ForeignKey(related_name='backend_analiseporperiodo_criacao_related', to=settings.AUTH_USER_MODEL, editable=False)),
            ],
            options={
                'verbose_name_plural': 'analises por periodo',
                'ordering': ['-ativo', '-periodo', '-data_hora_atualizacao', '-data_hora_criacao'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Configuracao',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('observacoes', models.CharField(max_length=255, blank=True, null=True)),
                ('ativo', models.BooleanField(default=True)),
                ('excluido', models.BooleanField(default=False)),
                ('data_hora_criacao', models.DateTimeField(auto_now_add=True)),
                ('data_hora_atualizacao', models.DateTimeField(auto_now=True)),
                ('chave', models.CharField(max_length=255)),
                ('valor', models.CharField(max_length=255)),
                ('usuario_atualizacao', models.ForeignKey(related_name='backend_configuracao_atualizacao_related', to=settings.AUTH_USER_MODEL, editable=False)),
                ('usuario_criacao', models.ForeignKey(related_name='backend_configuracao_criacao_related', to=settings.AUTH_USER_MODEL, editable=False)),
            ],
            options={
                'verbose_name_plural': 'configuracoes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Conta',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('observacoes', models.CharField(max_length=255, blank=True, null=True)),
                ('ativo', models.BooleanField(default=True)),
                ('excluido', models.BooleanField(default=False)),
                ('data_hora_criacao', models.DateTimeField(auto_now_add=True)),
                ('data_hora_atualizacao', models.DateTimeField(auto_now=True)),
                ('nome', models.CharField(max_length=255)),
                ('rendimento', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-ativo', 'nome', '-data_hora_atualizacao', '-data_hora_criacao'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('observacoes', models.CharField(max_length=255, blank=True, null=True)),
                ('ativo', models.BooleanField(default=True)),
                ('excluido', models.BooleanField(default=False)),
                ('data_hora_criacao', models.DateTimeField(auto_now_add=True)),
                ('data_hora_atualizacao', models.DateTimeField(auto_now=True)),
                ('nome', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'locais',
                'ordering': ['-ativo', 'nome', '-data_hora_atualizacao', '-data_hora_criacao'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Movimento',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('observacoes', models.CharField(max_length=255, blank=True, null=True)),
                ('ativo', models.BooleanField(default=True)),
                ('excluido', models.BooleanField(default=False)),
                ('data_hora_criacao', models.DateTimeField(auto_now_add=True)),
                ('data_hora_atualizacao', models.DateTimeField(auto_now=True)),
                ('operacao', models.CharField(max_length=2, choices=[('DE', 'Debito'), ('CR', 'Credito')])),
                ('valor', models.DecimalField(decimal_places=2, max_digits=9)),
            ],
            options={
                'ordering': ['-ativo', '-ponto__periodo', '-data_hora_atualizacao', '-data_hora_criacao'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('observacoes', models.CharField(max_length=255, blank=True, null=True)),
                ('ativo', models.BooleanField(default=True)),
                ('excluido', models.BooleanField(default=False)),
                ('data_hora_criacao', models.DateTimeField(auto_now_add=True)),
                ('data_hora_atualizacao', models.DateTimeField(auto_now=True)),
                ('data', models.DateField(default=datetime.datetime(2015, 4, 30, 13, 42, 48, 99764))),
                ('periodoAnterior', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.Periodo', blank=True)),
                ('usuario_atualizacao', models.ForeignKey(related_name='backend_periodo_atualizacao_related', to=settings.AUTH_USER_MODEL, editable=False)),
                ('usuario_criacao', models.ForeignKey(related_name='backend_periodo_criacao_related', to=settings.AUTH_USER_MODEL, editable=False)),
            ],
            options={
                'ordering': ['-ativo', '-data', '-data_hora_atualizacao', '-data_hora_criacao'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ponto',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('observacoes', models.CharField(max_length=255, blank=True, null=True)),
                ('ativo', models.BooleanField(default=True)),
                ('excluido', models.BooleanField(default=False)),
                ('data_hora_criacao', models.DateTimeField(auto_now_add=True)),
                ('data_hora_atualizacao', models.DateTimeField(auto_now=True)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=9)),
                ('periodo', models.DateField(default=datetime.datetime(2015, 4, 30, 13, 42, 48, 100918))),
                ('conta', models.ForeignKey(to='backend.Conta')),
                ('pontoAnterior', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.Ponto', blank=True)),
                ('usuario_atualizacao', models.ForeignKey(related_name='backend_ponto_atualizacao_related', to=settings.AUTH_USER_MODEL, editable=False)),
                ('usuario_criacao', models.ForeignKey(related_name='backend_ponto_criacao_related', to=settings.AUTH_USER_MODEL, editable=False)),
            ],
            options={
                'ordering': ['-ativo', '-periodo', '-data_hora_atualizacao', '-data_hora_criacao'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Rendimento',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('observacoes', models.CharField(max_length=255, blank=True, null=True)),
                ('ativo', models.BooleanField(default=True)),
                ('excluido', models.BooleanField(default=False)),
                ('data_hora_criacao', models.DateTimeField(auto_now_add=True)),
                ('data_hora_atualizacao', models.DateTimeField(auto_now=True)),
                ('conta', models.ForeignKey(to='backend.Conta', related_name='rendimento_conta')),
                ('usuario_atualizacao', models.ForeignKey(related_name='backend_rendimento_atualizacao_related', to=settings.AUTH_USER_MODEL, editable=False)),
                ('usuario_criacao', models.ForeignKey(related_name='backend_rendimento_criacao_related', to=settings.AUTH_USER_MODEL, editable=False)),
            ],
            options={
                'ordering': ['-ativo', '-data_hora_atualizacao', '-data_hora_criacao'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RendimentoPorPeriodo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('observacoes', models.CharField(max_length=255, blank=True, null=True)),
                ('ativo', models.BooleanField(default=True)),
                ('excluido', models.BooleanField(default=False)),
                ('data_hora_criacao', models.DateTimeField(auto_now_add=True)),
                ('data_hora_atualizacao', models.DateTimeField(auto_now=True)),
                ('periodo', models.DateField(default=datetime.datetime(2015, 4, 30, 13, 42, 48, 106255))),
                ('usuario_atualizacao', models.ForeignKey(related_name='backend_rendimentoporperiodo_atualizacao_related', to=settings.AUTH_USER_MODEL, editable=False)),
                ('usuario_criacao', models.ForeignKey(related_name='backend_rendimentoporperiodo_criacao_related', to=settings.AUTH_USER_MODEL, editable=False)),
            ],
            options={
                'verbose_name_plural': 'rendimentos por periodo',
                'ordering': ['-ativo', '-periodo', '-data_hora_atualizacao', '-data_hora_criacao'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('observacoes', models.CharField(max_length=255, blank=True, null=True)),
                ('ativo', models.BooleanField(default=True)),
                ('excluido', models.BooleanField(default=False)),
                ('data_hora_criacao', models.DateTimeField(auto_now_add=True)),
                ('data_hora_atualizacao', models.DateTimeField(auto_now=True)),
                ('categoria', models.CharField(max_length=2, choices=[('CO', 'Conta'), ('LO', 'Local')])),
                ('nome', models.CharField(max_length=255)),
                ('usuario_atualizacao', models.ForeignKey(related_name='backend_tipo_atualizacao_related', to=settings.AUTH_USER_MODEL, editable=False)),
                ('usuario_criacao', models.ForeignKey(related_name='backend_tipo_criacao_related', to=settings.AUTH_USER_MODEL, editable=False)),
            ],
            options={
                'ordering': ['-ativo', 'nome', '-data_hora_atualizacao', '-data_hora_criacao'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='movimento',
            name='ponto',
            field=models.ForeignKey(to='backend.Ponto'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='movimento',
            name='usuario_atualizacao',
            field=models.ForeignKey(related_name='backend_movimento_atualizacao_related', to=settings.AUTH_USER_MODEL, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='movimento',
            name='usuario_criacao',
            field=models.ForeignKey(related_name='backend_movimento_criacao_related', to=settings.AUTH_USER_MODEL, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='local',
            name='tipo',
            field=models.ForeignKey(to='backend.Tipo'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='local',
            name='usuario_atualizacao',
            field=models.ForeignKey(related_name='backend_local_atualizacao_related', to=settings.AUTH_USER_MODEL, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='local',
            name='usuario_criacao',
            field=models.ForeignKey(related_name='backend_local_criacao_related', to=settings.AUTH_USER_MODEL, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='conta',
            name='local',
            field=models.ForeignKey(to='backend.Local'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='conta',
            name='tipo',
            field=models.ForeignKey(to='backend.Tipo'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='conta',
            name='usuario_atualizacao',
            field=models.ForeignKey(related_name='backend_conta_atualizacao_related', to=settings.AUTH_USER_MODEL, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='conta',
            name='usuario_criacao',
            field=models.ForeignKey(related_name='backend_conta_criacao_related', to=settings.AUTH_USER_MODEL, editable=False),
            preserve_default=True,
        ),
    ]
