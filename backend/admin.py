from django.contrib import admin

from backend.forms import ValorForm, TipoForm, InstituicaoForm, InvestimentoForm
from backend.models import Valor, Tipo, Instituicao, Investimento


class ValorAdmin(admin.ModelAdmin):
    form = ValorForm
    list_display = ['valor', 'data', 'investimento', 'observacoes']
    list_filter = ['investimento', 'data_hora_atualizacao', 'data_hora_criacao']
    search_fields = ['valor', 'observacoes']
    date_hierarchy = 'data'
    exclude = ['usuario', 'excluido']
    
    def save_model(self, request, obj, form, change):
        #FIXME setar o usuario_criacao apenas se for nulo
        obj.usuario_criacao = request.user
        obj.usuario_atualizacao = request.user
        obj.save()
        
    def queryset(self, request):
        qs = super(ValorAdmin, self).queryset(request)
        return qs.filter(excluido=False)

admin.site.register(Valor, ValorAdmin)

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

    def queryset(self, request):
        qs = super(TipoAdmin, self).queryset(request)
        return qs.filter(excluido=False)

admin.site.register(Tipo, TipoAdmin)

class InstituicaoAdmin(admin.ModelAdmin):
    form = InstituicaoForm
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

    def queryset(self, request):
        qs = super(InstituicaoAdmin, self).queryset(request)
        return qs.filter(excluido=False)

admin.site.register(Instituicao, InstituicaoAdmin)

class InvestimentoAdmin(admin.ModelAdmin):
    form = InvestimentoForm
    list_display = ['nome', 'tipo', 'instituicao', 'observacoes']
    list_filter = ['tipo', 'instituicao', 'data_hora_atualizacao', 'data_hora_criacao']
    search_fields = ['nome', 'observacoes']
    date_hierarchy = 'data_hora_criacao'
    exclude = ['usuario', 'excluido']
    
    def save_model(self, request, obj, form, change):
        #FIXME setar o usuario_criacao apenas se for nulo
        obj.usuario_criacao = request.user
        obj.usuario_atualizacao = request.user
        obj.save()

    def queryset(self, request):
        qs = super(InvestimentoAdmin, self).queryset(request)
        return qs.filter(excluido=False)
    
admin.site.register(Investimento, InvestimentoAdmin)