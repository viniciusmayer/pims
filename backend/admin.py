from django.contrib import admin

from backend.forms import PontoForm, TipoForm, LocalForm, ContaForm, AnaliseForm, \
    PeriodoForm, MovimentoForm, RendimentoForm, ConfiguracaoForm, \
    RendimentoPorPeriodoForm, AnalisePorPeriodoForm
from backend.models import Ponto, Tipo, Local, Conta, Analise, Periodo, \
    Movimento, Rendimento, Configuracao, RendimentoPorPeriodo, AnalisePorPeriodo


class PontoAdmin(admin.ModelAdmin):
    form = PontoForm
    list_display = ['valor', 'periodo', 'nome_local', 'nome_tipo', 'nome_conta', 'diferenca', 'diferencaPercentual', 'pontoAnterior', 'observacoes']
    list_filter = ['conta__rendimento', 'conta__local', 'conta__tipo', 'conta__nome']
    search_fields = ['valor', 'observacoes']
    #date_hierarchy = 'periodo'
    exclude = ['excluido', 'conta']
    
    def save_model(self, request, obj, form, change):
        # FIXME setar o usuario_criacao apenas se for nulo
        obj.usuario_criacao = request.user
        obj.usuario_atualizacao = request.user
        obj.conta = obj.pontoAnterior.conta
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
    list_display = ['nome', 'tipo', 'local', 'rendimento', 'observacoes']
    list_filter = ['local', 'tipo', 'rendimento']
    search_fields = ['nome', 'observacoes']
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
    search_fields = ['observacoes']
    #date_hierarchy = 'periodo'
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

class AnalisePorPeriodoAdmin(admin.ModelAdmin):
    form = AnalisePorPeriodoForm
    list_display = ['periodo', 'diferenca', 'rendimento', 'resultado', 'resultadoPercentual', 'observacoes']
    search_fields = ['observacoes']
    #date_hierarchy = 'periodo'
    exclude = ['excluido']
    
    def save_model(self, request, obj, form, change):
        # FIXME setar o usuario_criacao apenas se for nulo
        obj.usuario_criacao = request.user
        obj.usuario_atualizacao = request.user
        obj.save()

    def get_queryset(self, request):
        qs = super(AnalisePorPeriodoAdmin, self).get_queryset(request)
        return qs.filter(excluido=False)
    
admin.site.register(AnalisePorPeriodo, AnalisePorPeriodoAdmin)

class PeriodoAdmin(admin.ModelAdmin):
    form = PeriodoForm
    list_display = ['data', 'periodoAnterior', 'observacoes']
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
    list_display = ['operacao', 'valor', 'periodo', 'nome_local', 'nome_tipo', 'nome_conta', 'observacoes']
    list_filter = ['operacao', 'ponto__conta__local', 'ponto__conta__tipo', 'ponto__conta__nome']
    search_fields = ['observacoes']
    # date_hierarchy = 'periodo'
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
    list_display = ['nome_local', 'nome_tipo', 'nome_conta', 'total', 'vezes', 'medio', 'mediaPercentual', 'observacoes']
    list_filter = ['conta__local', 'conta__tipo']
    search_fields = ['observacoes']
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

class RendimentoPorPeriodoAdmin(admin.ModelAdmin):
    form = RendimentoPorPeriodoForm
    list_display = ['periodo', 'total', 'vezes', 'medio', 'observacoes']
    search_fields = ['observacoes']
    #date_hierarchy = 'periodoTempo__data'
    exclude = ['excluido']
    
    def save_model(self, request, obj, form, change):
        # FIXME setar o usuario_criacao apenas se for nulo
        obj.usuario_criacao = request.user
        obj.usuario_atualizacao = request.user
        obj.save()

    def get_queryset(self, request):
        qs = super(RendimentoPorPeriodoAdmin, self).get_queryset(request)
        return qs.filter(excluido=False)
    
admin.site.register(RendimentoPorPeriodo, RendimentoPorPeriodoAdmin)

class ConfiguracaoAdmin(admin.ModelAdmin):
    form = ConfiguracaoForm
    list_display = ['chave', 'valor', 'observacoes', 'ativo']
    list_filter = ['ativo']
    search_fields = ['chave', 'valor', 'observacoes']
    exclude = ['excluido']
    
    def save_model(self, request, obj, form, change):
        obj.usuario_criacao = request.user
        obj.usuario_atualizacao = request.user
        obj.save()
    
    def get_queryset(self, request):
        qs = super(ConfiguracaoAdmin, self).get_queryset(request)
        return qs.filter(excluido=False)

admin.site.register(Configuracao, ConfiguracaoAdmin)
