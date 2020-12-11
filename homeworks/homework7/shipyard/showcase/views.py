from django.shortcuts import render
from showcase.models import SpaceShip

# Create your views here.

def ship_index(request):
    ships = SpaceShip.objects.all()
    context = {
        'ships': ships
    }
    return render(request, 'ship_index.html', context)

def ship_detail(request, pk):
    ship = SpaceShip.objects.get(pk=pk)
    context = {
        'ship': ship
    }
    return render(request, 'ship_detail.html', context)