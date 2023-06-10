from django.contrib import admin
from django.db.models.query_utils import Q

from backend.filters import StatusFilter
from backend.forms import (
    PontoForm,
    TipoForm,
    LocalForm,
    ContaForm,
    PeriodoForm,
    ConfiguracaoForm,
)
from backend.models import Registro, Tipo, Local, Conta, Periodo, Configuracao
from backend.tasks import Queue


class RegistroAdmin(admin.ModelAdmin):
    form = PontoForm
    list_display = [
        "valor",
        "periodo",
        "nome_local",
        "nome_tipo",
        "nome_conta",
        "diferenca",
        "diferencaPercentual",
        "pontoAnterior",
        "observacoes",
        "ativo",
    ]
    list_filter = [
        StatusFilter,
        "conta__rendimento",
        "conta__local",
        "conta__tipo",
        "conta__nome",
        "periodo",
    ]
    search_fields = ["periodo__data", "valor", "observacoes"]
    exclude = ["excluido", "pontoAnterior"]

    def save_model(self, request, obj, form, change):
        # FIXME setar o usuario_criacao apenas se for nulo
        obj.usuario_criacao = request.user
        obj.usuario_atualizacao = request.user
        obj.pontoAnterior = None
        p = Periodo.objects.filter(data__lt=obj.periodo.data).latest("data")
        pa = Registro.objects.filter(conta=obj.conta, periodo=p)
        if not p is None and pa.count() > 0:
            obj.pontoAnterior = pa.first()
        obj.save()
        queue = Queue()
        queue.notify()

    def get_queryset(self, request):
        qs = super(RegistroAdmin, self).get_queryset(request)
        return qs.filter(excluido=False)

    def get_form(self, request, obj=None, **kwargs):
        self.instance = obj
        return super(RegistroAdmin, self).get_form(request, obj=obj, **kwargs)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "conta":
            q = Q(ativo=True)
            if self.instance is None:
                kwargs["queryset"] = Conta.objects.filter(q).order_by(
                    "local__nome", "tipo__nome", "nome"
                )
            else:
                q = q | Q(id=self.instance.conta.id)
                kwargs["queryset"] = Conta.objects.filter(q).order_by(
                    "local__nome", "tipo__nome", "nome"
                )
        return super(RegistroAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs
        )


admin.site.register(Registro, RegistroAdmin)


class TipoAdmin(admin.ModelAdmin):
    form = TipoForm
    list_display = ["nome", "observacoes", "ativo"]
    list_filter = [StatusFilter]
    search_fields = ["nome", "observacoes"]
    exclude = ["excluido"]

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
    list_display = ["nome", "observacoes", "ativo"]
    list_filter = [StatusFilter]
    search_fields = ["nome", "observacoes"]
    exclude = ["excluido"]

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
    list_display = ["nome", "tipo", "local", "rendimento", "observacoes", "ativo"]
    list_filter = [StatusFilter, "local", "tipo", "rendimento"]
    search_fields = ["nome", "observacoes"]
    exclude = ["excluido"]

    def save_model(self, request, obj, form, change):
        # FIXME setar o usuario_criacao apenas se for nulo
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
        if db_field.name == "local":
            kwargs["queryset"] = Local.objects.filter(q).order_by("nome")
            if not self.instance is None:
                _q = q | Q(id=self.instance.local.id)
                kwargs["queryset"] = Local.objects.filter(_q).order_by("nome")
        if db_field.name == "tipo":
            kwargs["queryset"] = Tipo.objects.filter(q).order_by("nome")
            if not self.instance is None:
                _q = q | Q(id=self.instance.tipo.id)
                kwargs["queryset"] = Tipo.objects.filter(_q).order_by("nome")
        return super(ContaAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs
        )


admin.site.register(Conta, ContaAdmin)


class PeriodoAdmin(admin.ModelAdmin):
    form = PeriodoForm
    list_display = ["data", "periodoAnterior", "observacoes", "ativo"]
    list_filter = [StatusFilter]
    search_fields = ["observacoes"]
    date_hierarchy = "data"
    exclude = ["excluido"]

    def save_model(self, request, obj, form, change):
        # FIXME setar o usuario_criacao apenas se for nulo
        obj.usuario_criacao = request.user
        obj.usuario_atualizacao = request.user
        obj.save()

    def get_queryset(self, request):
        qs = super(PeriodoAdmin, self).get_queryset(request)
        return qs.filter(excluido=False)


admin.site.register(Periodo, PeriodoAdmin)


class ConfiguracaoAdmin(admin.ModelAdmin):
    form = ConfiguracaoForm
    list_display = ["chave", "valor", "observacoes", "ativo"]
    list_filter = [StatusFilter]
    search_fields = ["chave", "valor", "observacoes"]
    exclude = ["excluido"]

    def save_model(self, request, obj, form, change):
        obj.usuario_criacao = request.user
        obj.usuario_atualizacao = request.user
        obj.save()

    def get_queryset(self, request):
        qs = super(ConfiguracaoAdmin, self).get_queryset(request)
        return qs.filter(excluido=False)


admin.site.register(Configuracao, ConfiguracaoAdmin)
