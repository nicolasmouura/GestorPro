from django.shortcuts import render, get_object_or_404, redirect
from .models import Loja
from .forms import LojaForm


def home(request):
    return render(request, 'loja_app/home.html')


def lista_lojas(request):
    lojas = Loja.objects.all()
    return render(request, 'loja_app/loja_list.html', {'lojas': lojas})


def cadastrar_loja(request):
    if request.method == 'POST':
        form = LojaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_lojas')
    else:
        form = LojaForm()
    return render(request, 'loja_app/loja_form.html', {'form': form})


def editar_loja(request, pk):
    loja = get_object_or_404(Loja, pk=pk)
    if request.method == 'POST':
        form = LojaForm(request.POST, instance=loja)
        if form.is_valid():
            form.save()
            return redirect('listar_lojas')
    else:
        form = LojaForm(instance=loja)
    return render(request, 'loja_app/loja_form.html', {'form': form})


def excluir_loja(request, pk):
    loja = get_object_or_404(Loja, pk=pk)
    if request.method == 'POST':
        try:
            loja.delete()
            return redirect('listar_lojas')
        except:
            return render(
                request,
                'loja_app/loja_confirm_delete.html',
                {'loja': loja, 'erro': 'Não é possível excluir, existem produtos ou vendas vinculados.'}
            )
    return render(request, 'loja_app/loja_confirm_delete.html', {'loja': loja})
