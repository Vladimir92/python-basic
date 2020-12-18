from django.test import TestCase
from .models import Manufacturer, Internal, Weaponry, SpaceShip
from django.test import Client

# Create your tests here.
class TestModels(TestCase):
    
    def setUp(self):
        self.manufacturer = Manufacturer.objects.create(title="Zorgon Peterson", description="Orbiting Sirius 3, this company owns 3 big shipyards producing high-end racing vehicles")
        self.internal = Internal.objects.create(amount=4, typing="Main internals")
        self.weaponry = Weaponry.objects.create(amount=3, model="Plasma")
        self.ship = SpaceShip.objects.create(title="FerDeLance", 
                                             description="High-end rogue runner capable of doing massive amount of damage", 
                                             manufacturer=self.manufacturer, 
                                             internals=self.internal, 
                                             weapons=self.weaponry, 
                                             mass=120, 
                                             price=34_000_000)

    def tearDown(self):
        self.ship.delete()
        self.internal.delete()
        self.weaponry.delete()
        self.manufacturer.delete()

    def test_ship(self):
        self.assertEqual(str(self.ship.title), "FerDeLance")
        self.assertEqual(self.ship.manufacturer, self.manufacturer)
        self.assertEqual(int(self.internal.amount), 4)
        self.assertEqual(str(self.ship.weapons.model), "Plasma")
    

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.manufacturer = Manufacturer.objects.create(title="Core Dynamics", description="Federal ship manufacturing company")
        self.internal = Internal.objects.create(amount=6, typing="Main internals")
        self.weaponry = Weaponry.objects.create(amount=5, model="Thermal")
        self.ship = SpaceShip.objects.create(title="Federal Corvette", 
                                             description="Fleet-class battleship involving in military operations", 
                                             manufacturer=self.manufacturer, 
                                             internals=self.internal, 
                                             weapons=self.weaponry, 
                                             mass=190, 
                                             price=126_000_000)

    def tearDown(self):
        self.ship.delete()
        self.internal.delete()
        self.weaponry.delete()
        self.manufacturer.delete()

    def test_web(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 404)

        response = self.client.get('/ships/')
        self.assertEqual(response.status_code, 200)

    def test_web_context(self):
        response = self.client.get('/ships/')
        self.assertTrue('object_list' in response.context)
        self.assertTrue(self.ship in response.context['object_list'])