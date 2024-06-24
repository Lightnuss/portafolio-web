from django.shortcuts import render

# Create your views here.

def index(request):
    context={}
    return render(request, 'portafolio_web/index.html', context)

def about(request):
    context={}
    return render(request, 'portafolio_web/nosotros.html', context)

def contact(request):
    context={}
    return render(request, 'portafolio_web/contacto.html', context)

def menu(request):
    context={}
    return render(request, 'portafolio_web/curriculum.html', context)

def reservation(request):
    context={}
    return render(request, 'portafolio_web/login.html', context)

def service(request):
    context={}
    return render(request, 'portafolio_web/proyectos.html', context)

def service(request):
    context={}
    return render(request, 'portafolio_web/registro.html', context)
