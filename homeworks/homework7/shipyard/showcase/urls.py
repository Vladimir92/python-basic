from django.urls import path
from .views import ship_detail, ship_index


urlpatterns = [
    path("", ship_index, name="ship_index"),
    path("<int:pk>/", ship_detail, name="ship_detail"),
]
