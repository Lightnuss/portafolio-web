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
    path('cliente/list', views.cliente_list, name='cliente_list'),
    path('cliente/<int:pk>/', views.cliente_detail, name='cliente_detail'),
    path('cliente/new/', views.cliente_create, name='cliente_create'),
    path('cliente/<int:pk>/edit/', views.cliente_update, name='cliente_update'),
    path('cliente/<int:pk>/delete/', views.cliente_delete, name='cliente_delete'),
]