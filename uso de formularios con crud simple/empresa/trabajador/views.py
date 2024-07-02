from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from .models import Trabajador
from .forms import TrabajadorForm

def trabajador_list(request):
    trabajadores = Trabajador.objects.all()
    return render(request, 'trabajador/trabajador_list.html', {'trabajadores': trabajadores})

def trabajador_create(request):
    if request.method == 'POST':
        form = TrabajadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trabajador_list')
    else:
        form = TrabajadorForm()
    return render(request, 'trabajador/trabajador_form.html', {'form': form})

def trabajador_update(request, id):
    trabajador = get_object_or_404(Trabajador, id=id)
    if request.method == 'POST':
        form = TrabajadorForm(request.POST, instance=trabajador)
        if form.is_valid():
            form.save()
            return redirect('trabajador_list')
    else:
        form = TrabajadorForm(instance=trabajador)
    return render(request, 'trabajador/trabajador_form.html', {'form': form})

def trabajador_delete(request, id):
    trabajador = get_object_or_404(Trabajador, id=id)
    if request.method == 'POST':
        trabajador.delete()
        return redirect('trabajador_list')
    return render(request, 'trabajador/trabajador_confirm_delete.html', {'trabajador': trabajador})
