from django.db import models

# Create your models here.

class Manufacturer(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()

    def __str__(self):
        return self.title

class Internal(models.Model):
    amount = models.PositiveSmallIntegerField()
    typing = models.CharField(max_length=64, default="essential")

    def __str__(self):
        return self.typing + str(self.amount)

class Weaponry(models.Model):
    amount = models.PositiveSmallIntegerField()
    model = models.CharField(max_length=64, default="kinetic")

    def __str__(self):
        return self.model + str(self.amount)

class SpaceShip(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.PROTECT, db_index=True)
    internals = models.ForeignKey(Internal, on_delete=models.PROTECT)
    weapons = models.ForeignKey(Weaponry, on_delete=models.PROTECT)
    mass = models.PositiveIntegerField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.title

