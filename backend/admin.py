from django.contrib import admin
from django.db.models.query_utils import Q
from import_export import fields
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from backend.filters import StatusFilter
from backend.forms import PontoForm, TipoForm, LocalForm, ContaForm, AnaliseForm, \
    PeriodoForm, MovimentoForm, RendimentoForm, ConfiguracaoForm, \
    RendimentoPorPeriodoForm, AnalisePorPeriodoForm
from backend.models import Ponto, Tipo, Local, Conta, Analise, Periodo, \
    Movimento, Rendimento, Configuracao, RendimentoPorPeriodo, AnalisePorPeriodo
from backend.tasks import Queue


class PontoAdmin(admin.ModelAdmin):
    form = PontoForm
    list_display = ['valor', 'periodo', 'nome_local', 'nome_tipo', 'nome_conta', 'diferenca', 'diferencaPercentual', 'pontoAnterior', 'observacoes', 'ativo']
    list_filter = [StatusFilter, 'conta__rendimento', 'conta__local', 'conta__tipo', 'conta__nome']
    search_fields = ['periodo__data', 'valor', 'observacoes']
    exclude = ['excluido', 'pontoAnterior']
    
    def save_model(self, request, obj, form, change):
        # FIXME setar o usuario_criacao apenas se for nulo
        obj.usuario_criacao = request.user
        obj.usuario_atualizacao = request.user
        obj.pontoAnterior = None
        p = Periodo.objects.filter(data__lt=obj.periodo.data).latest('data')
        pa = Ponto.objects.filter(conta=obj.conta, periodo=p)
        if (not p is None and pa.count() > 0):
            obj.pontoAnterior = pa.first()
        obj.save()
        queue = Queue()
        queue.notify()
        
    def get_queryset(self, request):
        qs = super(PontoAdmin, self).get_queryset(request)
        return qs.filter(excluido=False)
    
    def get_form(self, request, obj=None, **kwargs):
        self.instance = obj
        return super(PontoAdmin, self).get_form(request, obj=obj, **kwargs)
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "conta":
            q = Q(ativo=True)
            if (self.instance is None):
                kwargs["queryset"] = Conta.objects.filter(q).order_by('local__nome', 'tipo__nome', 'nome')
            else:
                q = q | Q(id=self.instance.conta.id)
                kwargs["queryset"] = Conta.objects.filter(q).order_by('local__nome', 'tipo__nome', 'nome')
        return super(PontoAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Ponto, PontoAdmin)

class TipoAdmin(admin.ModelAdmin):
    form = TipoForm
    list_display = ['nome', 'observacoes', 'ativo']
    list_filter = [StatusFilter]
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
    list_display = ['nome', 'observacoes', 'ativo']
    list_filter = [StatusFilter]
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
    list_display = ['nome', 'tipo', 'local', 'rendimento', 'observacoes', 'ativo']
    list_filter = [StatusFilter, 'local', 'tipo', 'rendimento']
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

class AnaliseResource(resources.ModelResource):
    periodo = fields.Field()
    total = fields.Field()
    diferenca = fields.Field()
    diferencaPercentual = fields.Field() 
    
    class Meta:
        model = Analise
        export_order = ('periodo', 'total', 'diferenca', 'diferencaPercentual')
        
    def dehydrate_periodo(self, analise):
        return analise.periodo.data
    
    def dehydrate_total(self, analise):
        return analise.total
    
    def dehydrate_diferenca(self, analise):
        return analise.diferenca()
    
    def dehydrate_diferencaPercentual(self, analise):
        return analise.diferencaPercentual()

class AnaliseAdmin(ImportExportModelAdmin):
    resource_class = AnaliseResource
    form = AnaliseForm
    list_display = ['periodo', 'total', 'diferenca', 'diferencaPercentual', 'ativo']
    list_filter = [StatusFilter]
    #search_fields = ['observacoes']
    #exclude = ['excluido']
    
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
    list_display = ['periodo', 'diferenca', 'rendimento', 'resultado', 'resultadoPercentual', 'observacoes', 'ativo']
    list_filter = [StatusFilter]
    search_fields = ['observacoes']
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
    list_display = ['data', 'periodoAnterior', 'observacoes', 'ativo']
    list_filter = [StatusFilter]
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
    list_display = ['operacao', 'valor', 'periodo', 'nome_local', 'nome_tipo', 'nome_conta', 'observacoes', 'ativo']
    list_filter = [StatusFilter, 'operacao', 'ponto__conta__local', 'ponto__conta__tipo', 'ponto__conta__nome']
    search_fields = ['observacoes']
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
    list_display = ['nome_local', 'nome_tipo', 'nome_conta', 'total', 'vezes', 'medio', 'mediaPercentual', 'observacoes', 'ativo']
    list_filter = [StatusFilter, 'conta__local', 'conta__tipo']
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
    list_display = ['periodo', 'total', 'vezes', 'medio', 'observacoes', 'ativo']
    list_filter = [StatusFilter]
    search_fields = ['observacoes']
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
    list_filter = [StatusFilter]
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
