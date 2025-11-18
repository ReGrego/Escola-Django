from django.shortcuts import render, redirect
from .forms import ProdutoForm
from .models import Produto

def produto_new(request):
    if request.method == "POST":
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produtos:produto_lista')  #redireciona para a página de lista de produtos
    else:
        form = ProdutoForm()
    return render(request, 'produtos/produto_form.html', {'form': form})

def produto_lista(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/produto_lista.html', {'produtos':produtos})
