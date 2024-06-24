from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),

    # Cada una de mis paginas web:
    path('index',views.index, name='index'),
    path('nosotros',views.nosotros, name='nosotros'),
    path('contacto',views.contacto, name='contacto'),
    path('curriculum',views.curriculum, name='curriculum'),
    path('login',views.login, name='login'),
    path('proyectos',views.proyectos, name='proyectos'),
    path('registro',views.registro, name='registro'),
]