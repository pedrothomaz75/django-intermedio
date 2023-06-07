from django.shortcuts import render
from .forms import ContatoForm, ProdutoModelForm
from django.contrib import messages
from .models import Produto
from django.shortcuts import redirect

def index(request):
    context = {
        'produtos': Produto.objects.all()
    }
    return render(request, 'index.html', context)

def contato(request):
    # Só faz isso se o formulário tiver um submit
    form = ContatoForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid(): # Retorna se o formulário não tem erros
            form.send_mail() # Se o formulário for válido, enviei o email
            messages.success(request, 'Mensagem enviada com sucesso!')
            form = ContatoForm()
        else:
            messages.error(request, 'Erro ao enviar o email')

    context = {
        'form': form,
    }
    return render(request, 'contato.html', context)

def produto(request):
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':
            form = ProdutoModelForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()

                messages.success(request, 'Produto salvo com sucesso!')
                form = ProdutoModelForm() # Depois que a mensagem é enviada, ele deixa os fields em branco
            else:
                messages.error(request, 'Erro ao salvar o produto')
        else:
            form = ProdutoModelForm()
        context = {
            'form': form,
        }
        return render(request, 'produto.html', context)
    else:
        return redirect('index')