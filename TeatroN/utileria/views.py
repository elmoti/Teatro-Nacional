from django.shortcuts import redirect, render, get_object_or_404
from .models import Utileria, ReservaUtileria, ObraTeatro, DirectorObra
from .forms import UtileriaForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


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

@login_required
def reservar_utileria(request, utileria_id):
    utileria = get_object_or_404(Utileria, id=utileria_id)
    obras = ObraTeatro.objects.all()
    
    if request.method == 'POST':
        obra_id = request.POST.get('obra_id')
        obra = get_object_or_404(ObraTeatro, id=obra_id)
        
        if request.user.rol == 'Director_Obra':
            director_obra = get_object_or_404(DirectorObra, usuario=request.user)
       
            
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