from datetime import datetime
from decimal import Decimal
from django.db import models

from common.models import CommonInfo


class Tipo(CommonInfo):
    CATEGORIA = (
        ('CO', 'Conta'),
        ('LO', 'Local'),
    )
    categoria = models.CharField(max_length=2, choices=CATEGORIA)
    nome = models.CharField(max_length=255)
    
    class Meta:
        ordering = ['-ativo', 'nome', '-data_hora_atualizacao', '-data_hora_criacao']
        
    def __str__(self):
        return self.nome

class Local(CommonInfo):
    nome = models.CharField(max_length=255)

    tipo = models.ForeignKey(Tipo, limit_choices_to={'ativo':True, 'excluido':False, 'categoria':'LO'})

    class Meta:
        ordering = ['-ativo', 'nome', '-data_hora_atualizacao', '-data_hora_criacao']
        verbose_name_plural = 'locais'
        
    def __str__(self):
        return self.nome
    
class Conta(CommonInfo):
    nome = models.CharField(max_length=255)
    
    local = models.ForeignKey(Local, limit_choices_to={'ativo':True, 'excluido':False})
    tipo = models.ForeignKey(Tipo, limit_choices_to={'ativo':True, 'excluido':False, 'categoria':'CO'})
    
    class Meta:
        ordering = ['-ativo', 'nome', '-data_hora_atualizacao', '-data_hora_criacao']
    
    def __str__(self):
        return u'%s - %s - %s' % (self.local.nome, self.tipo.nome, self.nome)
    
class Periodo(CommonInfo):
    data = models.DateField(default=datetime.now())
    periodoAnterior = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, limit_choices_to={'ativo':True, 'excluido':False})
    
    class Meta:
        ordering = ['-ativo', '-data', '-data_hora_atualizacao', '-data_hora_criacao']
        
    def __str__(self):
        return str(self.data)    
    
class Ponto(CommonInfo):
    valor = models.DecimalField(max_digits=9, decimal_places=2)
    periodo = models.DateField(default=datetime.now())

    pontoAnterior = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, limit_choices_to={'ativo':True, 'excluido':False})
    conta = models.ForeignKey(Conta, limit_choices_to={'ativo':True, 'excluido':False})
    
    class Meta:
        ordering = ['-ativo', '-periodo', '-data_hora_atualizacao', '-data_hora_criacao']
        
    def nome_conta(self):
        return self.conta.nome
    nome_conta.short_description = 'Conta'
    
    def nome_local(self):
        return self.conta.local.nome
    nome_local.short_description = 'Local'
    
    def nome_tipo(self):
        return self.conta.tipo.nome
    nome_tipo.short_description = 'Tipo'

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
    
    def diferencaPercentual(self):
        if (not self.pontoAnterior is None):
            return round(((self.diferenca() / self.pontoAnterior.valor) * 100), 2)
        return None
    diferencaPercentual.short_description = 'diferenca percentual'
    
    def __str__(self):
        return u'%s - %s - %s - %s' % (self.periodo, self.nome_local(), self.nome_tipo(), self.nome_conta())

class Movimento(CommonInfo):
    OPERACAO = (
        ('DE', 'Debito'),
        ('CR', 'Credito'),
    )
    operacao = models.CharField(max_length=2, choices=OPERACAO)
    valor = models.DecimalField(max_digits=9, decimal_places=2)
    
    ponto = models.ForeignKey(Ponto, limit_choices_to={'ativo':True, 'excluido':False})
    
    class Meta:
        ordering = ['-ativo', '-data_hora_atualizacao', '-data_hora_criacao']
    
    def __str__(self):
        if (self.operacao is 'DE'):
            return '{0}{1} {2}'.format('-', self.valor, self.ponto)
        return '{0} {1}'.format(self.valor, self.ponto)
    
class Analise(CommonInfo):
    periodo = models.DateField(default=datetime.now())
    analiseAnterior = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, limit_choices_to={'ativo':True, 'excluido':False})
    
    class Meta:
        ordering = ['-ativo', '-periodo', '-data_hora_atualizacao', '-data_hora_criacao']
        
    def total(self):
        total = None
        pontos = Ponto.objects.filter(periodo=self.periodo)
        for ponto in pontos:
            if (total is None):
                total = 0
            total += ponto.valor
        return total
    
    def diferenca(self):
        if (not self.analiseAnterior is None):
            return self.total() - self.analiseAnterior.total()
        return None
    
    def diferencaPercentual(self):
        if (not self.analiseAnterior is None):
            return round(((self.diferenca() / self.analiseAnterior.total()) * 100), 2)
        return None
    diferencaPercentual.short_description = 'diferenca percentual'
    
    def __str__(self):
        return str(self.periodo)
    
class Rendimento(CommonInfo):
    conta = models.ForeignKey(Conta, limit_choices_to={'ativo':True, 'excluido':False})
        
    class Meta:
        ordering = ['-ativo', '-data_hora_atualizacao', '-data_hora_criacao']

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
    
    def vezes(self):
        pontos = Ponto.objects.filter(conta=self.conta)
        count = 0
        for ponto in pontos:
            dif = ponto.diferenca()
            if (not dif is None):
                count += 1
        return count
    
    def medio(self):
        total = self.total()
        if (not total is None):
            total /= self.vezes()
            return round(total, 2)
        return None
    medio.short_description = 'media'
    
    def mediaPercentual(self):
        total = None
        pontos = Ponto.objects.filter(conta=self.conta)
        for ponto in pontos:
            if (total is None):
                total = Decimal(0)
            dif = ponto.diferencaPercentual()
            if (not dif is None):
                total += ponto.diferencaPercentual()
        total /= self.vezes()
        return round(total, 2)
    mediaPercentual.short_description = 'media percentual'
