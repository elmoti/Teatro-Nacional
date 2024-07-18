from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Usuario
from django.contrib.auth.hashers import make_password
from django.contrib import messages

@login_required
def perfil(request):
    usuario = request.user
    return render(request, 'login_signup/perfil.html', {'usuario': usuario})

@login_required   
def editar_perfil(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        
        usuario.nombre = nombre
        usuario.email = email
        usuario.save()
        return redirect('perfil')
    return render(request, 'login_signup/editar_perfil.html', {'usuario': usuario})


def registro(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        contrasena = request.POST.get('contrasena')
        confirmar_contrasena = request.POST.get('confirmar_contrasena')
        
        if len(contrasena) < 5:
            messages.error(request, 'La contraseña debe tener al menos 5 caracteres.')
        elif contrasena.isdigit():
            messages.error(request, 'La contraseña no puede ser completamente numérica.')
        elif contrasena == nombre or contrasena == email:
            messages.error(request, 'La contraseña no puede ser similar a su información personal.')
        elif contrasena != confirmar_contrasena:
            messages.error(request, 'Las contraseñas no coinciden.')
        elif Usuario.objects.filter(email=email).exists():
            messages.error(request, 'El correo electrónico ya está en uso.')
        else:
            user = Usuario.objects.create(
                nombre = nombre,
                email = email,
                password = make_password(contrasena)
            )
            user.save()
            login(request, user)
            return redirect('login')
    return render(request, 'login_signup/registro.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def iniciar_sesion(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(request, email = email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Email o contraseña incorrectos.')
    
    return render(request, 'login_signup/login.html')

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