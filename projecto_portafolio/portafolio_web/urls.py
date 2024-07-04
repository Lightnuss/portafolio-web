from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('contacto', views.contacto, name='contacto'),
    path('curriculum', views.curriculum, name='curriculum'),
    path('login', views.login_view, name='login'),
    path('registro', views.register, name='registro'),
    path('logout', views.logout_view, name='logout'),
    path('proyectos', views.proyectos, name='proyectos'),
    path('proyectos/list', views.proyecto_list, name='proyecto_list'),
    path('proyectos/new/', views.proyecto_create, name='proyecto_create'),
    path('proyectos/<int:pk>/edit/', views.proyecto_update, name='proyecto_update'),
    path('proyectos/<int:pk>/delete/', views.proyecto_delete, name='proyecto_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


