# -*- coding: utf-8 -*-
from enum import Enum

from django.db import models
from django.utils import timezone

from common.models import CommonInfo


class Tipo(CommonInfo):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Local(CommonInfo):
    nome = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "locais"

    def __str__(self):
        return self.nome


class Conta(CommonInfo):
    nome = models.CharField(max_length=255)

    local = models.ForeignKey(Local, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome


class Periodo(CommonInfo):
    quando = models.DateField(default=timezone.now)

    def __str__(self):
        return self.quando.date().strftime("%Y-%m")


class Registro(CommonInfo):
    valor = models.DecimalField(max_digits=9, decimal_places=2)
    periodo = models.ForeignKey(Periodo, on_delete=models.PROTECT)
    conta = models.ForeignKey(Conta, on_delete=models.PROTECT)


class ChaveConfiguracaoEnum(Enum):
    TESTE = "Teste"


class Configuracao(CommonInfo):
    chave = models.CharField(choices=ChaveConfiguracaoEnum)
    valor = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "configuracoes"
