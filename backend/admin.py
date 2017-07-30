from django.contrib import admin
from django.db.models.query_utils import Q

from backend.filters import StatusFilter
from backend.forms import PontoForm, TipoForm, LocalForm, ContaForm, AnaliseForm, \
    MovimentoForm, RendimentoForm, ConfiguracaoForm, \
    RendimentoPorPeriodoForm, AnalisePorPeriodoForm
from backend.models import Ponto, Tipo, Local, Conta, Analise, \
    Movimento, Rendimento, Configuracao, RendimentoPorPeriodo, AnalisePorPeriodo
from backend.tasks import Queue


class PontoAdmin(admin.ModelAdmin):
    form = PontoForm
    list_display = ['valor', 'quando', 'nome_local', 'nome_tipo', 'nome_conta', 'diferenca', 'diferencaPercentual', 'observacoes', 'ativo']
    list_filter = [StatusFilter, 'conta__rendimento', 'conta__local', 'conta__tipo', 'conta__nome', 'quando']
    search_fields = ['quando', 'valor', 'observacoes']
    exclude = ['excluido']
    
    def nome_conta(self, obj):
        return obj.conta.nome
    nome_conta.short_description = 'Conta'
    
    def nome_local(self, obj):
        return obj.conta.local.nome
    nome_local.short_description = 'Local'
    
    def nome_tipo(self, obj):
        return obj.conta.tipo.nome
    nome_tipo.short_description = 'Tipo'
    
    def save_model(self, request, obj, form, change):
        obj.usuario_criacao = request.user
        obj.usuario_atualizacao = request.user
        obj.save()
        #queue = Queue()
        #queue.notify()
        
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
        obj.usuario_criacao = request.user
        obj.usuario_atualizacao = request.user
        obj.save()

    def get_queryset(self, request):
        qs = super(ContaAdmin, self).get_queryset(request)
        return qs.filter(excluido=False)

    def get_form(self, request, obj=None, **kwargs):
        self.instance = obj
        return super(ContaAdmin, self).get_form(request, obj=obj, **kwargs)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        q = Q(ativo=True)
        if db_field.name == 'local':
            kwargs["queryset"] = Local.objects.filter(q).order_by('nome')
            if (not self.instance is None):
                _q = q | Q(id=self.instance.local.id)
                kwargs["queryset"] = Local.objects.filter(_q).order_by('nome')
        if db_field.name == 'tipo':
            kwargs["queryset"] = Tipo.objects.filter(q).order_by('nome')
            if (not self.instance is None):
                _q = q | Q(id=self.instance.tipo.id)
                kwargs["queryset"] = Tipo.objects.filter(_q).order_by('nome')
        return super(ContaAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
    
admin.site.register(Conta, ContaAdmin)

class AnaliseAdmin(admin.ModelAdmin):
    form = AnaliseForm
    list_display = ['quando', 'total', 'diferenca', 'diferencaPercentual', 'ativo']
    list_filter = [StatusFilter]
    search_fields = ['observacoes']
    exclude = ['excluido']
    
    def save_model(self, request, obj, form, change):
        obj.usuario_criacao = request.user
        obj.usuario_atualizacao = request.user
        obj.save()

    def get_queryset(self, request):
        qs = super(AnaliseAdmin, self).get_queryset(request)
        return qs.filter(excluido=False)
    
admin.site.register(Analise, AnaliseAdmin)

class AnalisePorPeriodoAdmin(admin.ModelAdmin):
    form = AnalisePorPeriodoForm
    list_display = ['quando', 'diferenca', 'rendimento', 'resultado', 'resultadoPercentual', 'observacoes', 'ativo']
    list_filter = [StatusFilter]
    search_fields = ['observacoes']
    exclude = ['excluido']
    
    def save_model(self, request, obj, form, change):
        obj.usuario_criacao = request.user
        obj.usuario_atualizacao = request.user
        obj.save()

    def get_queryset(self, request):
        qs = super(AnalisePorPeriodoAdmin, self).get_queryset(request)
        return qs.filter(excluido=False)
    
admin.site.register(AnalisePorPeriodo, AnalisePorPeriodoAdmin)

class MovimentoAdmin(admin.ModelAdmin):
    form = MovimentoForm
    list_display = ['valor', 'quando', 'nome_local', 'nome_tipo', 'nome_conta', 'observacoes', 'ativo']
    list_filter = [StatusFilter, 'conta__local', 'conta__tipo', 'conta__nome']
    search_fields = ['observacoes']
    exclude = ['excluido']
    
    def nome_conta(self, obj):
        return obj.conta.nome
    nome_conta.short_description = 'Conta'
    
    def nome_local(self, obj):
        return obj.conta.local.nome
    nome_local.short_description = 'Local'
    
    def nome_tipo(self, obj):
        return obj.conta.tipo.nome
    nome_tipo.short_description = 'Tipo'
    
    def save_model(self, request, obj, form, change):
        obj.usuario_criacao = request.user
        obj.usuario_atualizacao = request.user
        obj.save()
        #queue = Queue()
        #queue.notify()

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
    
    def nome_conta(self, obj):
        return obj.conta.nome
    nome_conta.short_description = 'Conta'
    
    def nome_local(self, obj):
        return obj.conta.local.nome
    nome_local.short_description = 'Local'
    
    def nome_tipo(self, obj):
        return obj.conta.tipo.nome
    nome_tipo.short_description = 'Tipo'
    
    def save_model(self, request, obj, form, change):
        obj.usuario_criacao = request.user
        obj.usuario_atualizacao = request.user
        obj.save()

    def get_queryset(self, request):
        qs = super(RendimentoAdmin, self).get_queryset(request)
        return qs.filter(excluido=False)
    
admin.site.register(Rendimento, RendimentoAdmin)

class RendimentoPorPeriodoAdmin(admin.ModelAdmin):
    form = RendimentoPorPeriodoForm
    list_display = ['quando', 'total', 'vezes', 'medio', 'observacoes', 'ativo']
    list_filter = [StatusFilter]
    search_fields = ['observacoes']
    exclude = ['excluido']
    
    def save_model(self, request, obj, form, change):
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