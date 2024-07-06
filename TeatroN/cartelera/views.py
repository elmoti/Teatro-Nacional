from django.shortcuts import render, redirect, get_object_or_404
from utileria.models import Sala, ObraTeatro
from .models import Pelicula, ObraSala
from django.contrib import messages

def listar_obra(request):
    obras = ObraTeatro.objects.all()
    salas = Sala.objects.all()

    return render(request, 'cartelera/obras.html', {'obras': obras, 'salas': salas})

def listar_pelicula(request):
    peliculas = Pelicula.objects.all()
    return render(request, 'cartelera/peliculas.html', {'peliculas': peliculas})

def listar_cartelera(request):
    cartelera = ObraSala.objects.all()
    return render(request, 'cartelera/cartelera.html', {'cartelera': cartelera})

def agregar_obra_teatro(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        genero = request.POST.get('genero')
        imagen = request.FILES.get('imagen')
        
        obra_teatro = ObraTeatro(nombre = nombre, descripcion = descripcion, genero = genero, imagen = imagen)
        
        obra_teatro.save()
        return redirect('listar_obra')
    return render(request, 'cartelera/agregar_obra_teatro.html')

def editar_obra(request, obra_id):
    obra = get_object_or_404(ObraTeatro, id=obra_id)
    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        genero = request.POST['genero']
        imagen = request.FILES.get('imagen')
        
        obra.nombre = nombre
        obra.descripcion = descripcion
        obra.genero = genero
        obra.imagen = imagen
        
        obra.save()
        
        return redirect('listar_obra')
    return render(request, 'cartelera/editar_obra.html', {'obra': obra})

def eliminar_obra(request, obra_id):
    obra = get_object_or_404(ObraTeatro, id=obra_id)
    if request.method == 'POST':
        obra.delete()
        messages.success(request, 'Obra eliminada correctamente.')
        return redirect('listar_obra')
    return render(request, 'cartelera/eliminar_obra.html', {'obra': obra})

def agregar_pelicula(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        duracion = request.POST.get('duracion')
        realizador = request.POST.get('realizador')
        imagen = request.FILES.get('imagen')
        
        pelicula = Pelicula(nombre = nombre, duracion = duracion, realizador = realizador,imagen = imagen)
        pelicula.save()
        return redirect('listar_pelicula')
    
    return render(request, 'cartelera/agregar_pelicula.html')

def editar_pelicula(request, pelicula_id):
    pelicula = get_object_or_404(Pelicula, id=pelicula_id)
    
    if request.method == 'POST':
        nombre = request.POST['nombre']
        duracion = request.POST['duracion']
        realizador = request.POST['realizador']
        imagen = request.FILES.get('imagen')
        
        pelicula.nombre = nombre
        pelicula.duracion = duracion
        pelicula.realizador = realizador
        pelicula.imagen = imagen
        
        pelicula.save()
        return redirect('listar_pelicula')
    return render(request, 'cartelera/editar_pelicula.html', {'pelicula': pelicula})
    
def eliminar_pelicula(request, pelicula_id):
    pelicula = get_object_or_404(Pelicula, id=pelicula_id)
    if request.method == 'POST':
        pelicula.delete()
        messages.success(request, 'Pelicula eliminada correctamente.')
        return redirect('listar_pelicula')
    return render(request, 'cartelera/eliminar_pelicula.html', {'pelicula': pelicula})

