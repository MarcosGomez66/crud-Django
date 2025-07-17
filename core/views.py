from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from .forms import RegistroForm

# Create your views here.
def registroView(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('lista')
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
    return redirect('login')

@login_required
def home(request):
    return HttpResponse('Proyecto Django CRUD')

@login_required
def listaUsers(request):
    users = User.objects.all()
    return render(request, 'lista.html', {'users':users})

@login_required
def editar_user(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        form = RegistroForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('lista')
    else:
        form = RegistroForm(instance=user)
    return render(request, 'formulario.html', {'form': form, 'user': user})

@login_required
def eliminar_user(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        user.delete()
        return redirect('lista')
    return render(request, 'eliminar.html', {'user': user})