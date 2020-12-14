from django.shortcuts import render
from showcase.models import SpaceShip
from django.views.generic import ListView, DetailView

# Create your views here.

# def ship_index(request):
#     ships = SpaceShip.objects.all()
#     context = {
#         'ships': ships
#     }
#     return render(request, 'ship_index.html', context)

class ShipListView(ListView):
    model = SpaceShip
    template_name = 'ship_index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context

# def ship_detail(request, pk):
#     ship = SpaceShip.objects.get(pk=pk)
#     context = {
#         'ship': ship
#     }
#     return render(request, 'ship_detail.html', context)

class ShipDetailView(DetailView):
    model = SpaceShip

    template_name = 'ship_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context