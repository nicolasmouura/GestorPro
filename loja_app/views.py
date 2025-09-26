from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Loja
from .forms import LojaForm 
from django.shortcuts import get_object_or_404

# Create your views here.


# Função Listar lojas
def lista_lojas(request):
    lojas = Loja.objects.all()  # pega todas as lojas do banco
    return render(request, 'loja_app/loja_list.html', {'lojas': lojas})


# Função Cadastrar loja
def cadastrar_loja(request):
    if request.method == 'POST':  # se o formulário foi enviado
        form = LojaForm(request.POST)  # pega os dados enviados
        if form.is_valid():  # valida os dados
            form.save()  # salva no banco
            return redirect('lista_lojas')  # volta para a lista
    else:
        form = LojaForm()  # se for GET, apenas cria o formulário vazio
    return render(request, 'loja_app/loja_form.html', {'form': form})

# Função Excluir loja
def excluir_loja(request, pk):
    loja = get_object_or_404(Loja, pk=pk)  # pega a loja pelo id (ou dá erro 404)
    if request.method == 'POST':  # se o formulário de confirmação foi enviado
        try:
            loja.delete()  # tenta excluir a loja
            return redirect('lista_lojas')  # volta para a lista
        except:
            # se houver produtos ou vendas vinculados, mostra mensagem de erro
            return render(request, 'loja_app/loja_confirm_delete.html', {'loja': loja, 'erro': 'Não é possível excluir, existem produtos ou vendas vinculados.'})
    return render(request, 'loja_app/loja_confirm_delete.html', {'loja': loja})

#Função Editar Loja
def editar_loja(request, pk):
    loja = get_object_or_404(Loja, pk=pk)  # busca a loja ou dá erro 404
    if request.method == 'POST':
        form = LojaForm(request.POST, instance=loja)  # edita a loja existente
        if form.is_valid():
            form.save()
            return redirect('lista_lojas')
    else:
        form = LojaForm(instance=loja)  # abre o formulário preenchido com a loja
    return render(request, 'loja_app/loja_form.html', {'form': form})




