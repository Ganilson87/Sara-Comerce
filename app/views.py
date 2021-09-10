from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import produto
from django.core.paginator import Paginator
# Create your views here.


def produtoListView(request):
    produto_objects = produto.objects.all()
    pesquisar = request.GET.get('pesquisar')
    if pesquisar != '' and pesquisar is not None:
        produto_objects = produto.objects.filter(nome_prod__contains=pesquisar)
    #Paginas
    paginator = Paginator(produto_objects,6)
    pagina = request.GET.get('pagina')
    produto_objects = paginator.get_page(pagina)
    return render(request, 'index.html',{'produto_objects':produto_objects},)

class produtoDetailView(DetailView):
    model = produto
    template_name = "Produto_detail.html"
def checkout(request):
    return render(request, 'checkout.html')


    
