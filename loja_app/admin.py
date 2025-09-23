from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Loja

@admin.register(Loja)
class LojaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cnpj_loja', 'telefone', 'email')
    search_fields = ('nome', 'cnpj_loja')
