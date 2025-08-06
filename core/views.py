from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Publicacion, Tarea
from .forms import RegistroForm, PublicacionForm, TareaForm, EditarPerfilForm

# Create your views here.
def registroView(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registro exitoso.')
            return redirect('home')
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})

def loginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def logoutView(request):
    logout(request)
    return render(request, 'logout.html')

def home(request):
    return render(request, 'home.html')

@login_required
def listaUsers(request):
    users = User.objects.all()
    return render(request, 'lista.html', {'users':users})

@login_required
def perfil(request):
    return render(request, 'perfil.html', {'user': request.user})

@login_required
def editar_user(request):
    if request.method == 'POST':
        form = EditarPerfilForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, request.user)
            messages.success(request, 'Perfil actualizado exitosamente.')
            return redirect('perfil')
    else:
        form = EditarPerfilForm(instance=request.user)
    return render(request, 'editar.html', {'form': form})

@login_required
def eliminar_user(request):
    if request.method == 'POST':
        request.user.delete()
        logout(request)
        messages.success(request, 'Cuenta eliminada exitosamente.')
        return redirect('lista')
    return render(request, 'eliminar.html', {'user': request.user})

@login_required
def cambiar_contrasena(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Contraseña cambiada exitosamente.')
            return redirect('perfil')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'cambiar_passw.html', {'form': form})

@login_required
def publicaciones(request):
    # ver las publicaciones de todos los usuarios
    publicaciones = Publicacion.objects.all().order_by('-fecha_publicacion')
    return render(request, 'publicaciones.html', {'publicaciones': publicaciones})

@login_required
def crear_publicacion(request):
    if request.method == 'POST':
        form = PublicacionForm(request.POST)
        if form.is_valid():
            publicacion = form.save(commit=False)
            publicacion.autor = request.user
            publicacion.save()
            messages.success(request, 'Publicación creada exitosamente.')
            return redirect('home')
    else:
        form = PublicacionForm()
    return render(request, 'crear_publi.html', {'form': form})

@login_required
def editar_publicacion(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk, autor=request.user)
    if request.method == 'POST':
        form = PublicacionForm(request.POST, instance=publicacion)
        if form.is_valid():
            form.save()
            messages.success(request, 'Publicación actualizada exitosamente.')
            return redirect('publicaciones')
    else:
        form = PublicacionForm(instance=publicacion)
    return render(request, 'editar_publi.html', {'form': form})

@login_required
def eliminar_publicacion(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk, autor=request.user)
    if request.method == 'POST':
        publicacion.delete()
        messages.success(request, 'Publicación eliminada exitosamente.')
        return redirect('publicaciones')
    return render(request, 'eliminar_publi.html', {'publicacion': publicacion})