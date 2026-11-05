from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalogo, name='catalogo'),
    path('maquinaria/<int:pk>/', views.detalle_maquinaria, name='detalle_maquinaria'),
    path('cotizador/', views.ver_cotizador, name='ver_cotizador'),
    path('cotizador/agregar/<int:pk>/', views.agregar_al_cotizador, name='agregar_al_cotizador'),
    path('cotizador/eliminar/<int:pk>/', views.eliminar_del_cotizador, name='eliminar_del_cotizador'),
    path('cotizador/vaciar/', views.vaciar_cotizador, name='vaciar_cotizador'),
]