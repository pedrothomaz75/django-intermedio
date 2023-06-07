from django.db import models
from stdimage.models import StdImageField

# SIGNALS
from django.db.models import signals # Faz a alteração de dados do banco antes ou depois de ser opostos no próprio
from django.template.defaultfilters import slugify

"""
 - Basicamente, a classe Base vai ser pra saber as informações da minha classe, ela
    como sendo abstrata não vai ser colocada no banco de dados. A class age basicamente
    como "controle de versão".
"""

class Base(models.Model):
    criado = models.DateField('Data de criação', auto_now_add=True)
    modificado = models.DateField('Data de atualização', auto_now=True)
    ativo = models.BooleanField('Ativo ?', default=True)

    class Meta:
        abstract = True

class Produto(Base):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    estoque = models.IntegerField('Estoque')

    """
    Imagem vai receber método StdImageField('nome', upload_to='nome_do_diretório',
      variação={'nome da variação': (124, 124)})
    """
    imagem = StdImageField('Imagem', upload_to='produtos', variations={'thumb': (124, 124)})
    """
    Slug.models.SlugField('nome', tamanho_maximo_de_caracteres=100, pode ser em branco=True, editável=False)
        Slug são basicamente os nomes de produtos que ficam na URL, por exemplo 'www.sualoja/nome-do-produto.com.br
    """
    slug = models.SlugField('Slug', max_length=100, blank=False, editable=False)


    """
    Função que retorna 
    """
    def __str__(self):
        return self.nome
    
def produto_pre_save(signal, instance, sender, **kwargs):
    # Coloca o slug na url e deixa o nome do produto padronizado
    instance.slug = slugify(instance.nome)

# Antes de salvar, executa a função produto_pre_save quando o sender mandar um sinal
signals.pre_save.connect(produto_pre_save, sender=Produto)