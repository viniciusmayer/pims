from django.contrib.auth.models import User
from django.db import models


class CommonInfo(models.Model):
    observacoes = models.CharField(null=True, blank=True, max_length=255)

    ativo = models.BooleanField(default=True)
    excluido = models.BooleanField(default=False)
    
    data_hora_criacao = models.DateTimeField(auto_now_add=True, editable=False, blank=True)
    usuario_criacao = models.ForeignKey(User, editable=False, blank=False, related_name="%(app_label)s_%(class)s_criacao_related")
    data_hora_atualizacao = models.DateTimeField(auto_now=True, editable=False, blank=True)
    usuario_atualizacao = models.ForeignKey(User, editable=False, blank=False, related_name="%(app_label)s_%(class)s_atualizacao_related")
    
    class Meta:
        abstract = True
        
    def delete(self, using=None):
        self.excluido = True
        self.ativo = False
        models.Model.save(self, using=using)
