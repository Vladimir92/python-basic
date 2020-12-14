from django.urls import path
from .views import ShipListView, ShipDetailView


urlpatterns = [
    path("", ShipListView.as_view(), name="ship_index"),
    path("<int:pk>/", ShipDetailView.as_view(), name="ship_detail"),
]
