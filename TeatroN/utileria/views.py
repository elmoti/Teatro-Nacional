from django.shortcuts import redirect, render, get_object_or_404
from .models import Utileria, ReservaUtileria
from .forms import UtileriaForm
from .forms import ReservarUtileriaForm
from .forms import AprobarReservaForm

def home(request):
    return render(request, 'utileria/home.html')


def acercade(request):
    return render(request, 'utileria/acercade.html')

def listar_utilerias(request):
    utilerias = Utileria.objects.all()
    return render(request, 'utileria/listar_utilerias.html', {'utilerias': utilerias})

def detalle_utileria(request, utileria_id):
    utileria = get_object_or_404(Utileria, pk=utileria_id)

    if request.method == 'POST' and 'delete_utileria' in request.POST:
        utileria.delete()
        return redirect('listar_utilerias') 

    return render(request, 'utileria/detalle_utileria.html', {'utileria': utileria})


def agregar_utileria(request):
    if request.method == 'POST':
        form = UtileriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_utilerias') 
    else:
        form = UtileriaForm()

    return render(request, 'utileria/agregar_utileria.html', {'form': form})

def editar_utileria(request, utileria_id):
    utileria = get_object_or_404(Utileria, id=utileria_id)
    if request.method == 'POST':
        form = UtileriaForm(request.POST, instance=utileria)
        if form.is_valid():
            form.save()
            return redirect('detalle_utileria', utileria_id=utileria.id)
    else:
        form = UtileriaForm(instance=utileria)
    return render(request, 'utileria/editar_utileria.html', {'form': form, 'utileria': utileria})

def reservar_utileria(request):
    if request.method == 'POST':
        form = ReservarUtileriaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.director_obra = request.user
            reserva.save()
            return redirect('listar_utilerias')
    else:
        form = ReservarUtileriaForm()
    
    return render(request, 'utileria/reservar_utileria.html', {'form': form})

def gestionar_reservas(request):
    reservas_pendientes = ReservaUtileria.objects.filter(estado='pendiente')
    reservas_aprobadas = ReservaUtileria.objects.filter(estado='aprobada')
    reservas_denegadas = ReservaUtileria.objects.filter(estado='denegada')

    return render(request, 'utileria/gestionar_reservas.html', {
        'reservas_pendientes': reservas_pendientes,
        'reservas_aprobadas': reservas_aprobadas,
        'reservas_denegadas': reservas_denegadas,
    })


def cambiar_estado_reserva(request, reserva_id):
    reserva = get_object_or_404(ReservaUtileria, pk=reserva_id)
    
    if request.method == 'POST':
        form = AprobarReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect('gestionar_reservas')
    else:
        form = AprobarReservaForm(instance=reserva)
    
    return render(request, 'utileria/cambiar_estado_reserva.html', {'form': form})