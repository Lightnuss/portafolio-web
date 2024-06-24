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
