from django.contrib import admin

from backend.forms import PontoForm, TipoForm, LocalForm, ContaForm
from backend.models import Ponto, Tipo, Local, Conta


class PontoAdmin(admin.ModelAdmin):
    form = PontoForm
    list_display = ['valor', 'periodo', 'nome_conta', 'nome_tipo', 'nome_local', 'observacoes']
    list_filter = ['conta__tipo', 'conta__local', 'data_hora_atualizacao', 'data_hora_criacao']
    search_fields = ['valor', 'observacoes']
    date_hierarchy = 'periodo'
    exclude = ['usuario', 'excluido']
    
    def save_model(self, request, obj, form, change):
        #FIXME setar o usuario_criacao apenas se for nulo
        obj.usuario_criacao = request.user
        obj.usuario_atualizacao = request.user
        obj.save()
        
    def get_queryset(self, request):
        qs = super(PontoAdmin, self).get_queryset(request)
        return qs.filter(excluido=False)

admin.site.register(Ponto, PontoAdmin)

class TipoAdmin(admin.ModelAdmin):
    form = TipoForm
    list_display = ['nome', 'categoria', 'observacoes']
    list_filter = ['categoria', 'data_hora_atualizacao', 'data_hora_criacao']
    search_fields = ['nome', 'observacoes']
    date_hierarchy = 'data_hora_criacao'
    exclude = ['excluido']
    
    def save_model(self, request, obj, form, change):
        #FIXME setar o usuario_criacao apenas se for nulo
        obj.usuario_criacao = request.user
        obj.usuario_atualizacao = request.user
        obj.save()

    def get_queryset(self, request):
        qs = super(TipoAdmin, self).get_queryset(request)
        return qs.filter(excluido=False)

admin.site.register(Tipo, TipoAdmin)

class LocalAdmin(admin.ModelAdmin):
    form = LocalForm
    list_display = ['nome', 'tipo', 'observacoes']
    list_filter = ['tipo', 'data_hora_atualizacao', 'data_hora_criacao']
    search_fields = ['nome', 'observacoes']
    date_hierarchy = 'data_hora_criacao'
    exclude = ['usuario', 'excluido']
    
    def save_model(self, request, obj, form, change):
        #FIXME setar o usuario_criacao apenas se for nulo
        obj.usuario_criacao = request.user
        obj.usuario_atualizacao = request.user
        obj.save()

    def get_queryset(self, request):
        qs = super(LocalAdmin, self).get_queryset(request)
        return qs.filter(excluido=False)

admin.site.register(Local, LocalAdmin)

class ContaAdmin(admin.ModelAdmin):
    form = ContaForm
    list_display = ['nome', 'tipo', 'local', 'observacoes']
    list_filter = ['tipo', 'local', 'data_hora_atualizacao', 'data_hora_criacao']
    search_fields = ['nome', 'observacoes']
    date_hierarchy = 'data_hora_criacao'
    exclude = ['usuario', 'excluido']
    
    def save_model(self, request, obj, form, change):
        #FIXME setar o usuario_criacao apenas se for nulo
        obj.usuario_criacao = request.user
        obj.usuario_atualizacao = request.user
        obj.save()

    def get_queryset(self, request):
        qs = super(ContaAdmin, self).get_queryset(request)
        return qs.filter(excluido=False)
    
admin.site.register(Conta, ContaAdmin)