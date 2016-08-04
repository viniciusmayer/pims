# -*- coding: utf-8 -*-
from decimal import Decimal
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
    rendimento = models.BooleanField(default=False)
    
    local = models.ForeignKey(Local, limit_choices_to={'ativo':True, 'excluido':False})
    tipo = models.ForeignKey(Tipo, limit_choices_to={'ativo':True, 'excluido':False})
    
    class Meta:
        ordering = ['-ativo', 'nome', '-data_hora_atualizacao', '-data_hora_criacao']
    
    def __str__(self):
        return '%s - %s - %s' % (self.local.nome, self.tipo.nome, self.nome)
    
class Periodo(CommonInfo):
    data = models.DateField(default=timezone.now)
    periodoAnterior = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, limit_choices_to={'ativo':True, 'excluido':False})
    
    class Meta:
        ordering = ['-ativo', '-data', '-data_hora_atualizacao', '-data_hora_criacao']

    def __str__(self):
        return str(self.data)    
    
class Ponto(CommonInfo):
    valor = models.DecimalField(max_digits=9, decimal_places=2)

    periodo = models.ForeignKey(Periodo, limit_choices_to={'ativo':True, 'excluido':False})
    pontoAnterior = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, limit_choices_to={'ativo':True, 'excluido':False})
    conta = models.ForeignKey(Conta, limit_choices_to={'ativo':True, 'excluido':False})
    
    class Meta:
        ordering = ['-ativo', '-periodo__data', '-data_hora_atualizacao', '-data_hora_criacao']
        
    def nome_conta(self):
        return self.conta.nome
    nome_conta.short_description = 'Conta'
    
    def nome_local(self):
        return self.conta.local.nome
    nome_local.short_description = 'Local'
    
    def nome_tipo(self):
        return self.conta.tipo.nome
    nome_tipo.short_description = 'Tipo'

    #TODO testar 1º
    def diferenca(self):
        _diferenca = None
        if (not self.pontoAnterior is None):
            _diferenca = self.valor - self.pontoAnterior.valor
            movimentos = Movimento.objects.filter(ponto=self)
            for movimento in movimentos:
                # FIXME transformar numa Enum
                if (movimento.operacao == 'CR'):
                    _diferenca -= movimento.valor
                elif (movimento.operacao == 'DE'):
                    _diferenca += movimento.valor
        return _diferenca
    
    #TODO testar 2º
    def diferencaPercentual(self):
        if (not self.pontoAnterior is None):
            return round(((self.diferenca() / Decimal(self.pontoAnterior.valor)) * 100), 2)
        return None
    diferencaPercentual.short_description = 'diferenca percentual'
    
    def __str__(self):
        return '%s - %s - %s - %s' % (self.periodo.data, self.nome_local(), self.nome_tipo(), self.nome_conta())

class Movimento(CommonInfo):
    OPERACAO = (
        ('DE', 'Debito'),
        ('CR', 'Credito'),
    )
    operacao = models.CharField(max_length=2, choices=OPERACAO)
    valor = models.DecimalField(max_digits=9, decimal_places=2)
    
    ponto = models.ForeignKey(Ponto, limit_choices_to={'ativo':True, 'excluido':False})
    
    class Meta:
        ordering = ['-ativo', '-ponto__periodo__data', '-data_hora_atualizacao', '-data_hora_criacao']
    
    def __str__(self):
        if (self.operacao is 'DE'):
            return '{0}{1} {2}'.format('-', self.valor, self.ponto)
        return '{0} {1}'.format(self.valor, self.ponto)

    def periodo(self):
        return self.ponto.periodo

    def nome_conta(self):
        return self.ponto.nome_conta()
    nome_conta.short_description = 'Conta'
    
    def nome_local(self):
        return self.ponto.nome_local()
    nome_local.short_description = 'Local'
    
    def nome_tipo(self):
        return self.ponto.nome_tipo()
    nome_tipo.short_description = 'Tipo'
    
class Analise(CommonInfo):
    periodo = models.ForeignKey(Periodo, limit_choices_to={'ativo':True, 'excluido':False})
    analiseAnterior = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, limit_choices_to={'ativo':True, 'excluido':False})

    class Meta:
        ordering = ['-ativo', '-periodo__data', '-data_hora_atualizacao', '-data_hora_criacao']
        
    #TODO testar
    def total(self):
        total = None
        pontos = Ponto.objects.filter(periodo__data=self.periodo.data)
        for ponto in pontos:
            if (total is None):
                total = 0
            total += ponto.valor
        return total
    
    #TODO testar
    def diferenca(self):
        if (not self.analiseAnterior is None):
            return self.total() - self.analiseAnterior.total()
        return None
    
    #TODO testar
    def diferencaPercentual(self):
        if (not self.analiseAnterior is None):
            return round(((self.diferenca() / self.analiseAnterior.total()) * 100), 2)
        return None
    diferencaPercentual.short_description = 'diferenca percentual'
    
    def __str__(self):
        return str(self.periodo.data)
    
class AnalisePorPeriodo(CommonInfo):
    periodo = models.ForeignKey(Periodo, limit_choices_to={'ativo':True, 'excluido':False})

    class Meta:
        ordering = ['-ativo', '-periodo__data', '-data_hora_atualizacao', '-data_hora_criacao']
        verbose_name_plural = 'analises por periodo'

    #TODO testar
    def diferenca(self):
        analise = Analise.objects.get(periodo__data = self.periodo.data)
        return analise.diferenca()

    #TODO testar
    def rendimento(self):
        rendimento = RendimentoPorPeriodo.objects.get(periodo__data = self.periodo.data)
        return rendimento.total()
    
    #TODO testar
    def resultado(self):
        resultado = None
        diferenca = self.diferenca()
        total = self.rendimento()
        if ((not diferenca is None) and (not total is None)):
            resultado = diferenca - Decimal(total)
        return round(resultado, 2)

    #TODO testar
    def resultadoPercentual(self):
        resultado = None
        diferenca = self.diferenca()
        total = self.rendimento()
        if ((not diferenca is None) and (not total is None)):
            resultado = round(((diferenca / Decimal(total)) - 1), 2)
        return resultado
    resultadoPercentual.short_description = 'resultado percentual'

    def __str__(self):
        return str(self.periodo.data)

class Rendimento(CommonInfo):
    conta = models.ForeignKey(Conta, limit_choices_to={'ativo':True, 'excluido':False}, related_name='rendimento_conta')
        
    class Meta:
        ordering = ['-ativo', '-data_hora_atualizacao', '-data_hora_criacao']

    def nome_conta(self):
        return self.conta.nome
    nome_conta.short_description = 'Conta'
    
    def nome_local(self):
        return self.conta.local.nome
    nome_local.short_description = 'Local'
    
    def nome_tipo(self):
        return self.conta.tipo.nome
    nome_tipo.short_description = 'Tipo'

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
        if (not total is None):
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
        total /= self.vezes()
        return round(total, 2)
    mediaPercentual.short_description = 'media percentual'

class RendimentoPorPeriodo(CommonInfo):
    periodo = models.ForeignKey(Periodo, limit_choices_to={'ativo':True, 'excluido':False})
            
    class Meta:
        ordering = ['-ativo', '-periodo__data', '-data_hora_atualizacao', '-data_hora_criacao']
        verbose_name_plural = 'rendimentos por periodo'

    #TODO testar
    def total(self):
        total = None
        pontos = Ponto.objects.filter(periodo__data=self.periodo.data, conta__rendimento=True)
        for ponto in pontos:
            diferenca = ponto.diferenca()
            if (not diferenca is None):
                if (total is None):
                    total = Decimal(0)
                total += diferenca
        if (not total is None):
            total = round(total, 2)
        return total
    
    #TODO testar
    def vezes(self):
        pontos = Ponto.objects.filter(periodo__data=self.periodo.data, conta__rendimento=True)
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
        total = self.total()
        if (not total is None):
            total /= self.vezes()
            return round(total, 2)
        return None
    medio.short_description = 'media'
    
class Configuracao(CommonInfo):
    chave = models.CharField(max_length=255)
    valor = models.CharField(max_length=255)
    
    class Meta:
        verbose_name_plural = 'configuracoes'
