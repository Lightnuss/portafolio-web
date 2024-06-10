from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),

    # Cada una de mis paginas web:
    path('index',views.index, name='index'),
    path('nosotros',views.about, name='nosotros'),
    path('contacto',views.contact, name='contacto'),
    path('curriculum',views.menu, name='curriculum'),
    path('login',views.reservation, name='login'),
    path('proyectos',views.service, name='proyectos'),
]