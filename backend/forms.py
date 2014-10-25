from django import forms

from backend.models import Ponto, Tipo, Local, Conta, Analise, Periodo, \
    Movimento, Rendimento, RendimentoPorPeriodo, Configuracao


class PontoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PontoForm, self).__init__(*args, **kwargs)
        self.fields['observacoes'].widget = forms.Textarea()
        
    class Meta:
        model = Ponto
        exclude = [] 
        
class TipoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TipoForm, self).__init__(*args, **kwargs)
        self.fields['observacoes'].widget = forms.Textarea()
        
    class Meta:
        model = Tipo
        exclude = []

class LocalForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(LocalForm, self).__init__(*args, **kwargs)
        self.fields['observacoes'].widget = forms.Textarea()
        
    class Meta:
        model = Local
        exclude = []
        
class ContaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ContaForm, self).__init__(*args, **kwargs)
        self.fields['observacoes'].widget = forms.Textarea()
        
    class Meta:
        model = Conta
        exclude = []

class AnaliseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AnaliseForm, self).__init__(*args, **kwargs)
        self.fields['observacoes'].widget = forms.Textarea()
        
    class Meta:
        model = Analise
        exclude = []

class PeriodoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PeriodoForm, self).__init__(*args, **kwargs)
        self.fields['observacoes'].widget = forms.Textarea()
        
    class Meta:
        model = Periodo
        exclude = []

class MovimentoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MovimentoForm, self).__init__(*args, **kwargs)
        self.fields['observacoes'].widget = forms.Textarea()
        
    class Meta:
        model = Movimento
        exclude = []

class RendimentoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RendimentoForm, self).__init__(*args, **kwargs)
        self.fields['observacoes'].widget = forms.Textarea()
        
    class Meta:
        model = Rendimento
        exclude = []


class RendimentoPorPeriodoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RendimentoPorPeriodoForm, self).__init__(*args, **kwargs)
        self.fields['observacoes'].widget = forms.Textarea()
        
    class Meta:
        model = RendimentoPorPeriodo
        exclude = []
        

class ConfiguracaoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ConfiguracaoForm, self).__init__(*args, **kwargs)
        self.fields['observacoes'].widget = forms.Textarea()
        
    class Meta:
        model = Configuracao
        exclude = []
