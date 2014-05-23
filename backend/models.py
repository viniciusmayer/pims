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
        
    def __unicode__(self):
        return self.nome

    
class Local(CommonInfo):
    nome = models.CharField(max_length=255)

    tipo = models.ForeignKey(Tipo, limit_choices_to={'ativo':True, 'excluido':False, 'categoria':'LO'})

    class Meta:
        ordering = ['-ativo', 'nome', '-data_hora_atualizacao', '-data_hora_criacao']
        verbose_name_plural = 'locais'
        
    def __unicode__(self):
        return self.nome
    
class Conta(CommonInfo):
    nome = models.CharField(max_length=255)
    
    local = models.ForeignKey(Local, limit_choices_to={'ativo':True, 'excluido':False})
    tipo = models.ForeignKey(Tipo, limit_choices_to={'ativo':True, 'excluido':False, 'categoria':'CO'})
    
    class Meta:
        ordering = ['-ativo', 'nome', '-data_hora_atualizacao', '-data_hora_criacao']
    
    def __unicode__(self):
        return u'%s - %s - %s' % (self.nome, self.tipo.nome, self.local.nome)

class Ponto(CommonInfo):
    valor = models.DecimalField(max_digits=9, decimal_places=2)
    periodo = models.DateField(default=datetime.now())
    periodoAnterior = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, limit_choices_to={'ativo':True, 'excluido':False})
    
    conta = models.ForeignKey(Conta, limit_choices_to={'ativo':True, 'excluido':False})
    
    class Meta:
        ordering = ['-ativo', '-periodo', '-data_hora_atualizacao', '-data_hora_criacao']