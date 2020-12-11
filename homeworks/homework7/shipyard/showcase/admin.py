from django.contrib import admin
from .models import SpaceShip, Internal, Weaponry, Manufacturer
# Register your models here.

admin.site.register(SpaceShip)
admin.site.register(Internal)
admin.site.register(Weaponry)
admin.site.register(Manufacturer)