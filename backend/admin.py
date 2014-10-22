from django.contrib import admin

from backend.forms import PontoForm, TipoForm, LocalForm, ContaForm, AnaliseForm
from backend.models import Ponto, Tipo, Local, Conta, Analise


class PontoAdmin(admin.ModelAdmin):
    form = PontoForm
    list_display = ['valor', 'periodo', 'nome_conta', 'nome_tipo', 'nome_local', 'diferenca', 'diferencaPercentual', 'pontoAnterior', 'observacoes']
    list_filter = ['conta__nome', 'conta__tipo', 'conta__local']
    search_fields = ['valor', 'observacoes']
    date_hierarchy = 'periodo'
    exclude = ['excluido']
    
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
    list_filter = ['categoria']
    search_fields = ['nome', 'observacoes']
    #date_hierarchy = 'data_hora_criacao'
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
    list_filter = ['tipo']
    search_fields = ['nome', 'observacoes']
    #date_hierarchy = 'data_hora_criacao'
    exclude = ['excluido']
    
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
    list_filter = ['tipo', 'local']
    search_fields = ['nome', 'observacoes']
    #date_hierarchy = 'data_hora_criacao'
    exclude = ['excluido']
    
    def save_model(self, request, obj, form, change):
        #FIXME setar o usuario_criacao apenas se for nulo
        obj.usuario_criacao = request.user
        obj.usuario_atualizacao = request.user
        obj.save()

    def get_queryset(self, request):
        qs = super(ContaAdmin, self).get_queryset(request)
        return qs.filter(excluido=False)
    
admin.site.register(Conta, ContaAdmin)

class AnaliseAdmin(admin.ModelAdmin):
    form = AnaliseForm
    list_display = ['periodo', 'total', 'diferenca', 'diferencaPercentual', 'analiseAnterior', 'observacoes']
    #list_filter = ['periodo', 'observacoes']
    search_fields = ['observacoes']
    date_hierarchy = 'periodo'
    exclude = ['excluido']
    
    def save_model(self, request, obj, form, change):
        #FIXME setar o usuario_criacao apenas se for nulo
        obj.usuario_criacao = request.user
        obj.usuario_atualizacao = request.user
        obj.save()

    def get_queryset(self, request):
        qs = super(AnaliseAdmin, self).get_queryset(request)
        return qs.filter(excluido=False)
    
admin.site.register(Analise, AnaliseAdmin)