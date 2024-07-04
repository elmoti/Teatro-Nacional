from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm , UsuarioForm
from .forms import RegistroForm, EditarUsuarioForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Usuario
from django.contrib import messages

def perfil(request):
    usuario = request.user
    return render(request, 'login_signup/perfil.html', {'usuario': usuario})

def editar_perfil(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)

    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('perfil') 
    else:
        form = UsuarioForm(instance=usuario)
    context = {
        'form': form,
        'usuario': usuario
    }
    return render(request, 'login_signup/editar_perfil.html', context)


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
@user_passes_test(lambda u: u.is_superuser)
def editar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    if request.method == 'POST':
        form = EditarUsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario actualizado correctamente.')
            return redirect('lista_usuarios')
    else:
        form = EditarUsuarioForm(instance=usuario)
    return render(request, 'login_signup/editar_usuario.html', {'form': form, 'usuario': usuario})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def procesar_usuarios(request):
    if request.method == 'POST':
        usuarios_seleccionados = request.POST.getlist('usuarios_seleccionados')
        for usuario_id in usuarios_seleccionados:
            usuario = get_object_or_404(Usuario, id=usuario_id)
            usuario.delete()
        messages.success(request, 'Usuarios procesados correctamente.')
        return redirect('lista_usuarios')
    else:
        return redirect('lista_usuarios')

@login_required
@user_passes_test(lambda u: u.is_superuser)    
def eliminar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    if request.method == 'POST':
        usuario.delete()
        messages.success(request, 'Usuario eliminado correctamente.')
        return redirect('lista_usuarios')
    return render(request, 'login_signup/eliminar_usuario.html', {'usuario': usuario})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'login_signup/lista_usuarios.html', {'usuarios': usuarios})