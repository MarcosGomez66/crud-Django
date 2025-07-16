from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('lista/', views.listaUsers, name='lista'),
    path('crear/', views.crear_user, name='crear'),
    path('editar/<int:id>/', views.editar_user, name='editar'),
    path('eliminar/<int:id>/', views.eliminar_user, name='eliminar'),
]