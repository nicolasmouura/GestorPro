
#Classe LojaForm

from django import forms
from .models import Loja

class LojaForm(forms.ModelForm):
    class Meta:
        model = Loja  # diz que esse formulário é baseado no model Loja
        fields = ['cnpj_loja', 'nome', 'telefone', 'email']  # campos que vão aparecer
