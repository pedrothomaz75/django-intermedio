from django.contrib import admin
from .models import Produto

# Fazendo o registro da list usando o conceito de decorator
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque', 'slug', 'criado', 'modificado', 'ativo')
    