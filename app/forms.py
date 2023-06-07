from django import forms
from django.core.mail.message import EmailMessage
from .models import Produto

class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome')
    email = forms.IntegerField(label='E-mail')
    assunto = forms.CharField(label='Assunto')
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea()) # Textarea = caixa de texto com várias linhas

    def send_mail(self):
        nome = self.cleaned_data['Nome']
        email = self.cleaned_data['E-mail']
        assunto = self.cleaned_data['Assunto']
        mensagem = self.cleaned_data['Mensagem']

        conteudo = f'Nome: {nome}\nE-mail: {email}\nAssunto: {assunto}\nMensagem: {mensagem}'

        # Estrutura do email
        mail = EmailMessage(
            subject='E-mail enviado pelo sistema ',
            body=conteudo,
            from_email='contato@seudominio.com.br',
            to={'outro@seudominio.com.br'},
            headers={'Reply-To': email},
        )

        # Envio do email
        mail.send()

class ProdutoModelForm(forms.ModelForm):
    # Passando meta-dados
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'estoque', 'imagem']