# -*- coding: utf-8 -*-
from decimal import Decimal
from django.db import models
from enum import Enum

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
    rendimento = models.BooleanField(default=False)
    
    local = models.ForeignKey(Local)
    tipo = models.ForeignKey(Tipo)
    
    class Meta:
        ordering = ['-ativo', 'nome', '-data_hora_atualizacao', '-data_hora_criacao']
    
    def __str__(self):
        return '%s - %s - %s' % (self.local.nome, self.tipo.nome, self.nome)
    
class Ponto(CommonInfo):
    valor = models.DecimalField(max_digits=9, decimal_places=2)
    quando = models.DateField()

    conta = models.ForeignKey(Conta)
    
    class Meta:
        ordering = ['-ativo', '-quando', '-data_hora_atualizacao', '-data_hora_criacao']
    
    def __str__(self):
        return '%s - %s - %s - %s' % (self.quando, self.nome_local(), self.nome_tipo(), self.nome_conta())
        
    #TODO testar 1º
    def diferenca(self):
        _diferenca = None
        _pontoAnterior = Ponto.objects.filter(quando__lt=self.quando).order_by('-quando').first()
        if (not _pontoAnterior is None):
            _diferenca = self.valor - _pontoAnterior.valor
            #FIXME Movimento.ponto -> Movimento.conta&quando: consultar movimentos entre duas datas 
            movimentos = Movimento.objects.filter(quando=self.quando, conta=self.conta)
            for movimento in movimentos:
                _diferenca += movimento.valor
        return _diferenca
    
    #TODO testar 2º
    def diferencaPercentual(self):
        _diferencaPercentual = None
        _pontoAnterior = Ponto.objects.filter(quando__lt=self.quando).order_by('-quando').first()
        if (not _pontoAnterior is None):
            _diferencaPercentual = round(((self.diferenca() / Decimal(_pontoAnterior.valor)) * 100), 2)
        return _diferencaPercentual
    diferencaPercentual.short_description = 'diferenca percentual'

class Movimento(CommonInfo):
    valor = models.DecimalField(max_digits=9, decimal_places=2)
    quando = models.DateField()

    conta = models.ForeignKey(Conta)
    
    class Meta:
        ordering = ['-ativo', '-quando', '-data_hora_atualizacao', '-data_hora_criacao']
    
    def __str__(self):
        if (self.operacao is 'DE'):
            return '{0}{1} {2}'.format('-', self.valor, self.quando)
        return '{0} {1}'.format(self.valor, self.quando)

class Analise(CommonInfo):
    quando = models.DateField() 
    total = models.DecimalField(max_digits=9, decimal_places=2, null=True)

    class Meta:
        ordering = ['-ativo', '-quando', '-data_hora_atualizacao', '-data_hora_criacao']
    
    def __str__(self):
        return str(self.quando)
        
    #TODO testar
    def diferenca(self):
        _analiseAnterior = Analise.objects.filter(quando__lt=self.quando).order_by('-quando').first()
        if (not _analiseAnterior is None):
            return self.total - _analiseAnterior.total
        return None
    
    #TODO testar
    def diferencaPercentual(self):
        _analiseAnterior = Analise.objects.filter(quando__lt=self.quando).order_by('-quando').first()
        if (not _analiseAnterior is None):
            return round(((self.diferenca() / _analiseAnterior.total) * 100), 2)
        return None
    diferencaPercentual.short_description = 'diferenca percentual'
    
class AnalisePorPeriodo(CommonInfo):
    quando = models.DateField()

    class Meta:
        ordering = ['-ativo', '-quando', '-data_hora_atualizacao', '-data_hora_criacao']
        verbose_name_plural = 'analises por periodo'

    def __str__(self):
        return str(self.quando)

    #TODO testar
    def diferenca(self):
        analise = Analise.objects.get(quando = self.quando)
        return analise.diferenca()

    #TODO testar
    def rendimento(self):
        rendimento = RendimentoPorPeriodo.objects.get(quando = self.quando)
        return rendimento.total
    
    #TODO testar
    def resultado(self):
        resultado = None
        diferenca = self.diferenca()
        total = self.rendimento()
        if ((not diferenca is None) and (not total is None)):
            resultado = round(diferenca - Decimal(total), 2)
        return resultado

    #TODO testar
    def resultadoPercentual(self):
        resultado = None
        diferenca = self.diferenca()
        total = self.rendimento()
        if ((not diferenca is None) and (not total is None)):
            resultado = round(((diferenca / Decimal(total)) - 1), 2)
        return resultado
    resultadoPercentual.short_description = 'resultado percentual'

class Rendimento(CommonInfo):
    conta = models.ForeignKey(Conta, related_name='rendimento_conta')
        
    class Meta:
        ordering = ['-ativo', '-data_hora_atualizacao', '-data_hora_criacao']

    #TODO testar
    def total(self):
        total = None
        pontos = Ponto.objects.filter(conta=self.conta)
        for ponto in pontos:
            if (total is None):
                total = Decimal(0)
            diferenca = ponto.diferenca()
            if (not diferenca is None):
                total += diferenca
        return round(total, 2)
    
    #TODO testar
    def vezes(self):
        pontos = Ponto.objects.filter(conta=self.conta)
        count = 0
        for ponto in pontos:
            dif = ponto.diferenca()
            if (not dif is None):
                count += 1
        return count
    
    #TODO testar
    def medio(self):
        total = self.total()
        if (not total is None and self.vezes() > 0):
            total /= self.vezes()
            return round(total, 2)
        return None
    medio.short_description = 'media'
    
    #TODO testar
    def mediaPercentual(self):
        total = None
        pontos = Ponto.objects.filter(conta=self.conta)
        for ponto in pontos:
            if (total is None):
                total = Decimal(0)
            dif = ponto.diferencaPercentual()
            if (not dif is None):
                total += Decimal(dif)
        if (not total is None and self.vezes() > 0):
            total /= self.vezes()
        return round(total, 2)
    mediaPercentual.short_description = 'media percentual'

class RendimentoPorPeriodo(CommonInfo):
    quando = models.DateField()
    total = models.DecimalField(max_digits=9, decimal_places=2, null=True)
            
    class Meta:
        ordering = ['-ativo', '-quando', '-data_hora_atualizacao', '-data_hora_criacao']
        verbose_name_plural = 'rendimentos por periodo'

    #TODO testar
    def vezes(self):
        pontos = Ponto.objects.filter(quando=self.quando, conta__rendimento=True)
        count = None
        for ponto in pontos:
            diferenca = ponto.diferenca()
            if (not diferenca is None):
                if (count is None):
                    count = 0
                count += 1
        return count
    
    #TODO testar
    def medio(self):
        total = self.total
        vezes = self.vezes()
        if (not total is None and not vezes is None):
            total /= self.vezes()
            return round(total, 2)
        return None
    medio.short_description = 'media'
    
class ConfiguracaoEnum(Enum):
    dbURL = 'jdbc:postgresql://localhost:5432/pims'
    dbUser = 'pims'
    dbPassword = 'viniciusmayer'
    queueHost = 'localhost'
    queueName = 'pims'

class Configuracao(CommonInfo):
    chave = models.CharField(max_length=255)
    valor = models.CharField(max_length=255)
    
    class Meta:
        verbose_name_plural = 'configuracoes'