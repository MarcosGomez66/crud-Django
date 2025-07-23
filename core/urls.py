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
    path('publicacion/', views.publicaciones, name='publicaciones'),
    path('publicacion/nuevo/', views.crear_publicacion, name='crear_publicacion'),
    path('publicacion/editar/<int:pk>/', views.editar_publicacion, name='editar_publicacion'),
    path('publicacion/eliminar/<int:pk>/', views.eliminar_publicacion, name='eliminar_publicacion'),
]