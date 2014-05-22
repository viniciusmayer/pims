from django import forms

from backend.models import Valor, Tipo, Instituicao, Investimento


class ValorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ValorForm, self).__init__(*args, **kwargs)
        self.fields['observacoes'].widget = forms.Textarea()
        
    class Meta:
        model = Valor
        
class TipoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TipoForm, self).__init__(*args, **kwargs)
        self.fields['observacoes'].widget = forms.Textarea()
        
    class Meta:
        model = Tipo

class InstituicaoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(InstituicaoForm, self).__init__(*args, **kwargs)
        self.fields['observacoes'].widget = forms.Textarea()
        
    class Meta:
        model = Instituicao
        
class InvestimentoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(InvestimentoForm, self).__init__(*args, **kwargs)
        self.fields['observacoes'].widget = forms.Textarea()
        
    class Meta:
        model = Investimento
