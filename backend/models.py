from datetime import datetime
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
        return u'%s - %s - %s' % (self.nome, self.tipo.nome, self.local.nome)
    
class Ponto(CommonInfo):
    valor = models.DecimalField(max_digits=9, decimal_places=2)
    periodo = models.DateField(default=datetime.now())
    #FIXME change from periodoAnterior to pontoAnterior 
    periodoAnterior = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, limit_choices_to={'ativo':True, 'excluido':False})
    
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
    
    def __str__(self):
        return str(self.periodo)
    
class Analise(CommonInfo):
    periodo = models.DateField(default=datetime.now())
    #FIXME change from periodoAnterior to analiseAnterior
    periodoAnterior = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, limit_choices_to={'ativo':True, 'excluido':False})
    
    class Meta:
        ordering = ['-ativo', '-periodo', '-data_hora_atualizacao', '-data_hora_criacao']
        
    def total(self):
        total = None
        pontos = Ponto.objects.filter(periodo = self.periodo)
        for ponto in pontos:
            if (total is None):
                total = 0
            total += ponto.valor
        return total
    total.short_description = 'Total'
    
    def diferenca(self):
        if (not self.periodoAnterior is None):
            return self.total() - self.periodoAnterior.total()
        return None
    
    def diferencaPercentual(self):
        if (not self.periodoAnterior is None):
            return round(((self.diferenca() / self.periodoAnterior.total()) * 100), 2)
        return None
    diferencaPercentual.short_description = 'Diferenca percentual'
    
    def __str__(self):
        return str(self.periodo)