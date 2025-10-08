from django.shortcuts import render, redirect, get_object_or_404
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
            return redirect('lista_lojas')
    else:
        form = LojaForm()
    return render(request, 'loja_app/cadastrar_form.html', {'form': form})


def editar_loja(request, id):
    loja = get_object_or_404(Loja, id=id)
    if request.method == 'POST':
        form = LojaForm(request.POST, instance=loja)
        if form.is_valid():
            form.save()
            return redirect('lista_lojas')
    else:
        form = LojaForm(instance=loja)
    return render(request, 'loja_app/editar_form.html', {'form': form})


def excluir_loja(request, id):
    loja = get_object_or_404(Loja, id=id)
    if request.method == 'POST':
        loja.delete()
        return redirect('lista_lojas')
    return render(request, 'loja_app/excluir_loja.html', {'loja': loja})


