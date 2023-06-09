# -*- coding: utf-8 -*-
from decimal import Decimal
from enum import Enum

from django.db import models
from django.utils import timezone

from common.models import CommonInfo


class Tipo(CommonInfo):
    nome = models.CharField(max_length=255)

    class Meta:
        ordering = ['-ativo', 'nome', '-data_hora_atualizacao', '-data_hora_criacao']

    def __str__(self):
        return self.nome


class Local(CommonInfo):
    nome = models.CharField(max_length=255)

    class Meta:
        ordering = ['-ativo', 'nome', '-data_hora_atualizacao', '-data_hora_criacao']
        verbose_name_plural = 'locais'

    def __str__(self):
        return self.nome


class Conta(CommonInfo):
    nome = models.CharField(max_length=255)

    local = models.ForeignKey(Local, on_delete=models.PROTECT)

    class Meta:
        ordering = ['-ativo', 'nome', '-data_hora_atualizacao', '-data_hora_criacao']

    def __str__(self):
        return self.nome


class Periodo(CommonInfo):
    data = models.DateField(default=timezone.now)

    class Meta:
        ordering = ['-ativo', '-data', '-data_hora_atualizacao', '-data_hora_criacao']

    def __str__(self):
        return str(self.data)


class Ponto(CommonInfo):
    valor = models.DecimalField(max_digits=9, decimal_places=2)
    periodo = models.ForeignKey(Periodo, on_delete=models.PROTECT)
    conta = models.ForeignKey(Conta, on_delete=models.PROTECT)

    class Meta:
        ordering = ['-ativo', '-periodo__data', '-data_hora_atualizacao', '-data_hora_criacao']


class ChaveConfiguracaoEnum(Enum):
    TESTE = 'Teste'


class Configuracao(CommonInfo):
    chave = models.CharField(choices=ChaveConfiguracaoEnum)
    valor = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'configuracoes'
