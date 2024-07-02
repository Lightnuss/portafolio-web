from django.shortcuts import render

# Create your views here.

def index(request):
    context={}
    return render(request, 'portafolio_web/index.html', context)

def nosotros(request):
    context={}
    return render(request, 'portafolio_web/nosotros.html', context)

def contacto(request):
    context={}
    return render(request, 'portafolio_web/contacto.html', context)

def curriculum(request):
    context={}
    return render(request, 'portafolio_web/curriculum.html', context)

def login(request):
    context={}
    return render(request, 'portafolio_web/login.html', context)

def proyectos(request):
    context={}
    return render(request, 'portafolio_web/proyectos.html', context)

def registro(request):
    context={}
    return render(request, 'portafolio_web/registro.html', context)

# clientes/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente
from .forms import ClienteForm

def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'portafolio_web/cliente_list.html', {'clientes': clientes})

def cliente_detail(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    return render(request, 'portafolio_web/cliente_detail.html', {'cliente': cliente})

def cliente_create(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')
    else:
        form = ClienteForm()
    return render(request, 'portafolio_web/cliente_form.html', {'form': form})

def cliente_update(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'portafolio_web/cliente_form.html', {'form': form})

def cliente_delete(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('cliente_list')
    return render(request, 'portafolio_web/cliente_confirm_delete.html', {'cliente': cliente})

