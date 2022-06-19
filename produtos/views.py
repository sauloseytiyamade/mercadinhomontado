from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Produto
from .forms import ProdutoForm


@login_required
def produtos_list(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos.html', {'produtos': produtos})

@login_required
def produtos_create(request):
    form = ProdutoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('produtos_list')
    return render(request, 'produtos_form.html', {'form': form, 'titleSubmitButton': 'Adicionar'})

@login_required
def produtos_update(request, id):
    produto = get_object_or_404(Produto, pk=id)
    form = ProdutoForm(request.POST or None, instance=produto)

    if form.is_valid():
        form.save()
        return redirect('produtos_list')
    
    return render(request, 'produtos_form.html', {'form': form, 'titleSubmitButton': 'Atualizar'})
    
@login_required
def produtos_delete(request, id):
    produto = get_object_or_404(Produto, pk=id)

    if request.method == 'POST':
        produto.delete()
        return redirect('produtos_list')
    
    return render(request, 'produto_delete_confirm.html', {'produto': produto})

@login_required
def mylogout(request):
    logout(request)
    return redirect('home')