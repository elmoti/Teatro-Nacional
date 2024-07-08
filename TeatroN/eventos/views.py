from django.shortcuts import render, redirect
from .models import ObraSala
from utileria.models import ObraTeatro, Sala
from cartelera.models import Pelicula
from django.contrib.auth.decorators import login_required


def lista_evento(request):
    eventos = ObraSala.objects.all()
    return render(request, 'eventos/eventos.html', {'eventos': eventos})

@login_required
def agregar_obrasala(request):
    if request.method == 'POST':
        obra_teatro_id = request.POST.get('obra_teatro')
        sala_id = request.POST.get('sala')
        fecha = request.POST.get('fecha')
        hora = request.POST.get('hora')
        
        if obra_teatro_id:
            obra_teatro = ObraTeatro.objects.get(id=obra_teatro_id)
            obra_sala = ObraSala(obra_teatro=obra_teatro, sala_id=sala_id, fecha=fecha, hora=hora)
        
        obra_sala.save()
        return redirect('lista_evento')
    
    obras_teatro = ObraTeatro.objects.all()
    salas = Sala.objects.all()
    
    return render(request, 'eventos/agregar_obra.html', {
        'obras_teatro': obras_teatro,
        'salas': salas
    })

@login_required
def agregar_obrapelicula(request):
    if request.method == 'POST':
        pelicula_id = request.POST.get('pelicula')
        sala_id = request.POST.get('sala')
        fecha = request.POST.get('fecha')
        hora = request.POST.get('hora')
        
        if pelicula_id:
            pelicula = Pelicula.objects.get(id=pelicula_id)
            obra_sala = ObraSala(pelicula=pelicula, sala_id=sala_id, fecha=fecha, hora=hora)
        
        obra_sala.save()
        return redirect('lista_evento')
    
    peliculas = Pelicula.objects.all()
    salas = Sala.objects.all()
    
    return render(request, 'eventos/agregar_pelicula.html', {
        'peliculas': peliculas,
        'salas': salas
    })

