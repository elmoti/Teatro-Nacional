from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm , RegistroForm
from django.contrib.auth.decorators import login_required
from .models import Usuario

@login_required
def perfil(request):
    usuario = request.user
    return render(request, 'login_signup/perfil.html', {'usuario': usuario})

@login_required   
def editar_perfil(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    
    if request.method == 'POST':
        usuario.nombre = request.POST.get('nombre')
        usuario.email = request.POST.get('email')
        
        usuario.save()
        
        return redirect('lista_usuarios')
    return render(request, 'login_signup/editar_perfil.html', {'usuario': usuario})


def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login') 
    else:
        form = RegistroForm()
    return render(request, 'login_signup/registro.html', {'form': form})


def iniciar_sesion(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Usuario o contraseña incorrectos.')
    else:
        form = LoginForm()
    
    return render(request, 'login_signup/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def editar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    
    if request.method == 'POST':
        usuario.nombre = request.POST.get('nombre')
        usuario.email = request.POST.get('email')
        usuario.rol = request.POST.get('rol')
        
        usuario.save()
        
        return redirect('lista_usuarios')
    return render(request, 'login_signup/editar_usuario.html', {'usuario': usuario})

@login_required   
def eliminar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    if request.method == 'POST':
        usuario.delete()
        
        return redirect('lista_usuarios')
    return render(request, 'login_signup/eliminar_usuario.html', {'usuario': usuario})

@login_required
def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'login_signup/lista_usuarios.html', {'usuarios': usuarios})