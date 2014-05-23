from datetime import datetime
from django.db import models

from common.models import CommonInfo


class Tipo(CommonInfo):
    CATEGORIA = (
        ('IN', 'Investimento'),
        ('IS', 'Instituicao'),
    )
    categoria = models.CharField(max_length=2, choices=CATEGORIA)
    nome = models.CharField(max_length=255)
    
    class Meta:
        ordering = ['-ativo', 'nome', '-data_hora_atualizacao', '-data_hora_criacao']
        
    def __unicode__(self):
        return self.nome

    
class Instituicao(CommonInfo):
    nome = models.CharField(max_length=255)

    tipo = models.ForeignKey(Tipo, limit_choices_to={'ativo':True, 'excluido':False, 'categoria':'IS'})

    class Meta:
        ordering = ['-ativo', 'nome', '-data_hora_atualizacao', '-data_hora_criacao']
        verbose_name_plural = 'instituicoes'
        
    def __unicode__(self):
        return self.nome
    
class Investimento(CommonInfo):
    nome = models.CharField(max_length=255)
    
    instituicao = models.ForeignKey(Instituicao, limit_choices_to={'ativo':True, 'excluido':False})
    tipo = models.ForeignKey(Tipo, limit_choices_to={'ativo':True, 'excluido':False, 'categoria':'IN'})
    
    class Meta:
        ordering = ['-ativo', 'nome', '-data_hora_atualizacao', '-data_hora_criacao']
    
    def __unicode__(self):
        return u'%s - %s - %s' % (self.nome, self.tipo.nome, self.instituicao.nome)

class Valor(CommonInfo):
    valor = models.DecimalField(max_digits=9, decimal_places=2)
    data = models.DateField(default=datetime.now())
    
    investimento = models.ForeignKey(Investimento, limit_choices_to={'ativo':True, 'excluido':False})
    
    class Meta:
        ordering = ['-ativo', '-data', '-data_hora_atualizacao', '-data_hora_criacao']
        verbose_name_plural = 'valores'
