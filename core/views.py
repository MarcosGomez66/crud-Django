from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import User
from .forms import UserForm

# Create your views here.
def home(request):
    return HttpResponse('Hola mundo')

def listaUsers(request):
    users = User.objects.all()
    return render(request, 'lista.html', {'users':users})

def crear_user(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista')
    return render(request, 'formulario.html', {'form':form})

def editar_user(request, id):
    user = get_object_or_404(User, id=id)
    form = UserForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        return redirect('lista')
    return render(request, 'formulario.html', {'form':form})

def eliminar_user(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        user.delete()
        return redirect('lista')
    return render(request, 'eliminar.html', {'user':user})