from django.db import models

# Create your models here.

class Manufacturer(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()

class Internal(models.Model):
    amount = models.PositiveSmallIntegerField()

class Weaponry(models.Model):
    amount = models.PositiveSmallIntegerField()

class SpaceShip(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.PROTECT, db_index=True)
    mass = models.PositiveIntegerField()
    price = models.PositiveIntegerField()

