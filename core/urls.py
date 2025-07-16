from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('lista/', views.listaUsers, name='lista'),
    path('registro/', views.registroView, name='registro'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('editar/<int:id>/', views.editar_user, name='editar'),
    path('eliminar/<int:id>/', views.eliminar_user, name='eliminar'),
]