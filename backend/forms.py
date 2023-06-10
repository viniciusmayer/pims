from django import forms

from backend.models import Registro, Tipo, Local, Conta, Periodo, Configuracao


class PontoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PontoForm, self).__init__(*args, **kwargs)
        self.fields["observacoes"].widget = forms.Textarea()

    class Meta:
        model = Registro
        exclude = []


class TipoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TipoForm, self).__init__(*args, **kwargs)
        self.fields["observacoes"].widget = forms.Textarea()

    class Meta:
        model = Tipo
        exclude = []


class LocalForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(LocalForm, self).__init__(*args, **kwargs)
        self.fields["observacoes"].widget = forms.Textarea()

    class Meta:
        model = Local
        exclude = []


class ContaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ContaForm, self).__init__(*args, **kwargs)
        self.fields["observacoes"].widget = forms.Textarea()

    class Meta:
        model = Conta
        exclude = []


class PeriodoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PeriodoForm, self).__init__(*args, **kwargs)
        self.fields["observacoes"].widget = forms.Textarea()

    class Meta:
        model = Periodo
        exclude = []


class ConfiguracaoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ConfiguracaoForm, self).__init__(*args, **kwargs)
        self.fields["observacoes"].widget = forms.Textarea()

    class Meta:
        model = Configuracao
        exclude = []
