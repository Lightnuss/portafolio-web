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

# def proyectos(request):
#     context={}
#     return render(request, 'portafolio_web/proyectos.html', context)

def proyectos(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'portafolio_web/proyectos.html', {'proyectos': proyectos})

def registro(request):
    context={}
    return render(request, 'portafolio_web/registro.html', context)


from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm, UserLoginForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Cuenta creada para {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'portafolio_web/registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, 'Usuario o contraseña incorrectos')
    else:
        form = UserLoginForm()
    return render(request, 'portafolio_web/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Proyecto
from .forms import ProyectoForm

@login_required
def proyecto_list(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'portafolio_web/proyecto_list.html', {'proyectos': proyectos})

@login_required
def proyecto_create(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST, request.FILES)
        if form.is_valid():
            proyecto = form.save(commit=False)
            proyecto.creado_por = request.user
            proyecto.save()
            return redirect('proyecto_list')
    else:
        form = ProyectoForm()
    return render(request, 'portafolio_web/proyecto_form.html', {'form': form})

@login_required
def proyecto_update(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)
    if request.method == 'POST':
        form = ProyectoForm(request.POST, request.FILES, instance=proyecto)
        if form.is_valid():
            form.save()
            return redirect('proyecto_list')
    else:
        form = ProyectoForm(instance=proyecto)
    return render(request, 'portafolio_web/proyecto_form.html', {'form': form})

@login_required
def proyecto_delete(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)
    if request.method == 'POST':
        proyecto.delete()
        return redirect('proyecto_list')
    return render(request, 'portafolio_web/proyecto_confirm_delete.html', {'proyecto': proyecto})


from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactoForm

def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            # Aquí puedes manejar el envío del formulario, como enviar un correo electrónico
            return HttpResponse('¡Envío del formulario exitoso!')
    else:
        form = ContactoForm()
    return render(request, 'portafolio_web/contacto.html', {'form': form})

