from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('lista/', views.listaUsers, name='lista'),
    path('registro/', views.registroView, name='registro'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('perfil/', views.perfil, name='perfil'),
    path('perfil/editar/', views.editar_user, name='editar'),
    path('perfil/eliminar/', views.eliminar_user, name='eliminar'),
    path('perfil/cambiar_contraseña/', views.cambiar_contrasena, name='cambiar_contrasena'),
]