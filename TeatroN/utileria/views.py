from django.shortcuts import redirect, render, get_object_or_404
from .models import Utileria, ReservaUtileria, ObraTeatro
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime

def yearcontext(request):
    year = datetime.now().year
    return render(request, 'utileria/base.html',{'year': year} )

def home(request):
    year = datetime.now().year
    return render(request, 'utileria/home.html')


def acercade(request):
    return render(request, 'utileria/acercade.html')

@login_required
def listar_utilerias(request):
    utilerias = Utileria.objects.all()
    return render(request, 'utileria/listar_utilerias.html', {'utilerias': utilerias})

@login_required
def detalle_utileria(request, utileria_id):
    utileria = get_object_or_404(Utileria, pk=utileria_id)

    if request.method == 'POST' and 'delete_utileria' in request.POST:
        utileria.delete()
        return redirect('listar_utilerias') 

    return render(request, 'utileria/detalle_utileria.html', {'utileria': utileria})

@login_required
def agregar_utileria(request):
    if request.method == 'POST':
        codigo = request.POST.get('codigo')
        descripcion = request.POST.get('descripcion')
        nueva_utileria = Utileria(codigo=codigo, descripcion=descripcion)
        nueva_utileria.save()
        return redirect('listar_utilerias')
    return render(request, 'utileria/agregar_utileria.html')

@login_required
def editar_utileria(request, utileria_id):
    utileria = get_object_or_404(Utileria, id=utileria_id)
    if request.method == 'POST':
        utileria.codigo = request.POST.get('codigo')
        utileria.descripcion = request.POST.get('descripcion')
        utileria.save()
        return redirect('detalle_utileria', utileria_id=utileria.id)
    return render(request, 'utileria/editar_utileria.html', {'utileria': utileria})

@login_required
def reservar_utileria(request, utileria_id):
    utileria = get_object_or_404(Utileria, id=utileria_id)
    obras = ObraTeatro.objects.all()
    
    if request.method == 'POST':
        obra_id = request.POST.get('obra_id')
        obra = get_object_or_404(ObraTeatro, id=obra_id)
        director_obra = request.user  
        fecha_reserva = request.POST.get('fecha_reserva')
        estado = request.POST.get('estado', 'pendiente')
        reserva = ReservaUtileria(
            obra=obra,
            utileria=utileria,
            director_obra=director_obra,
            fecha_reserva=fecha_reserva,
            estado=estado
        )
        reserva.save()
        return redirect('detalle_utileria', utileria_id=utileria.id)
    
    context = {
        'utileria': utileria,
        'obras': obras,
    }
    return render(request, 'utileria/reservar_utileria.html', context)

@login_required
def lista_reserva_utileria(request):
    reservas = ReservaUtileria.objects.all().order_by('estado', 'fecha_reserva')
    
    for reserva in reservas:
        if reserva.estado == 'aprobada':
            reserva.estado_color = 'text-green-500'
        elif reserva.estado == 'pendiente':
            reserva.estado_color = 'text-red-500'
        else:
            reserva.estado_color = 'text-red-500'
            
    context = {
        'reservas': reservas,
    }
    return render(request, 'utileria/lista_reserva_utileria.html', context)

@login_required
def editar_reserva(request, reserva_id):
    reserva = get_object_or_404(ReservaUtileria, id=reserva_id)
    
    if request.method == 'POST':
        reserva.estado = request.POST.get('estado')
        reserva.save()
        return redirect('lista_reserva_utileria')
    
    return render(request, 'utileria/editar_reserva.html', { 'reserva': reserva })

@login_required
def eliminar_reserva(request, reserva_id):
    reserva = get_object_or_404(ReservaUtileria, id= reserva_id)
    if request.method == 'POST':
        reserva.delete()
        messages.success(request, 'Reserva eliminada correctamente.')
        return redirect('lista_reserva_utileria')
    return render(request, 'utileria/eliminar_reserva.html', {'reserva': reserva})

@login_required
def eliminar_utileria(request, utileria_id):
    utileria = get_object_or_404(Utileria, id= utileria_id)
    reserva = ReservaUtileria.objects.all()
    if request.method == 'POST':
        utileria.delete()
        messages.success(request, 'Reserva eliminada correctamente.')
        return redirect('detalle_utileria')
    return render(request, 'utileria/eliminar_utileria.html', {'utileria': utileria , 'reserva': reserva})
