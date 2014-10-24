from django.contrib import admin

from backend.forms import PontoForm, TipoForm, LocalForm, ContaForm, AnaliseForm, \
    PeriodoForm, MovimentoForm, RendimentoForm
from backend.models import Ponto, Tipo, Local, Conta, Analise, Periodo, \
    Movimento, Rendimento


class PontoAdmin(admin.ModelAdmin):
    form = PontoForm
    list_display = ['valor', 'periodo', 'nome_local', 'nome_tipo', 'nome_conta', 'diferenca', 'diferencaPercentual', 'pontoAnterior', 'observacoes']
    list_filter = ['conta__local', 'conta__tipo', 'conta__nome']
    search_fields = ['valor', 'observacoes']
    date_hierarchy = 'periodo'
    exclude = ['excluido']
    
    def save_model(self, request, obj, form, change):
        # FIXME setar o usuario_criacao apenas se for nulo
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
    # date_hierarchy = 'data_hora_criacao'
    exclude = ['excluido']
    
    def save_model(self, request, obj, form, change):
        # FIXME setar o usuario_criacao apenas se for nulo
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
    # date_hierarchy = 'data_hora_criacao'
    exclude = ['excluido']
    
    def save_model(self, request, obj, form, change):
        # FIXME setar o usuario_criacao apenas se for nulo
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
    list_filter = ['local', 'tipo']
    search_fields = ['nome', 'observacoes']
    # date_hierarchy = 'data_hora_criacao'
    exclude = ['excluido']
    
    def save_model(self, request, obj, form, change):
        # FIXME setar o usuario_criacao apenas se for nulo
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
    # list_filter = ['periodo', 'observacoes']
    search_fields = ['observacoes']
    date_hierarchy = 'periodo'
    exclude = ['excluido']
    
    def save_model(self, request, obj, form, change):
        # FIXME setar o usuario_criacao apenas se for nulo
        obj.usuario_criacao = request.user
        obj.usuario_atualizacao = request.user
        obj.save()

    def get_queryset(self, request):
        qs = super(AnaliseAdmin, self).get_queryset(request)
        return qs.filter(excluido=False)
    
admin.site.register(Analise, AnaliseAdmin)

class PeriodoAdmin(admin.ModelAdmin):
    form = PeriodoForm
    list_display = ['data', 'periodoAnterior', 'observacoes']
    # list_filter = ['periodo', 'observacoes']
    search_fields = ['observacoes']
    date_hierarchy = 'data'
    exclude = ['excluido']
    
    def save_model(self, request, obj, form, change):
        # FIXME setar o usuario_criacao apenas se for nulo
        obj.usuario_criacao = request.user
        obj.usuario_atualizacao = request.user
        obj.save()

    def get_queryset(self, request):
        qs = super(PeriodoAdmin, self).get_queryset(request)
        return qs.filter(excluido=False)
    
admin.site.register(Periodo, PeriodoAdmin)

class MovimentoAdmin(admin.ModelAdmin):
    form = MovimentoForm
    list_display = ['operacao', 'valor', 'ponto', 'observacoes']
    list_filter = ['operacao']
    search_fields = ['observacoes']
    # date_hierarchy = 'data'
    exclude = ['excluido']
    
    def save_model(self, request, obj, form, change):
        # FIXME setar o usuario_criacao apenas se for nulo
        obj.usuario_criacao = request.user
        obj.usuario_atualizacao = request.user
        obj.save()

    def get_queryset(self, request):
        qs = super(MovimentoAdmin, self).get_queryset(request)
        return qs.filter(excluido=False)
    
admin.site.register(Movimento, MovimentoAdmin)

class RendimentoAdmin(admin.ModelAdmin):
    form = RendimentoForm
    list_display = ['conta', 'total', 'vezes', 'medio', 'mediaPercentual', 'observacoes']
    # list_filter = ['conta']
    search_fields = ['observacoes']
    # date_hierarchy = 'data'
    exclude = ['excluido']
    
    def save_model(self, request, obj, form, change):
        # FIXME setar o usuario_criacao apenas se for nulo
        obj.usuario_criacao = request.user
        obj.usuario_atualizacao = request.user
        obj.save()

    def get_queryset(self, request):
        qs = super(RendimentoAdmin, self).get_queryset(request)
        return qs.filter(excluido=False)
    
admin.site.register(Rendimento, RendimentoAdmin)
