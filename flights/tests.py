# Create your tests here.
from django.test import TestCase
from flights.models import City
from flights.models import Airline

# models test
class FlightTest(TestCase):

    def create_city(self, name="test"):
        return City.objects.create(name=name)

    def test_city_creation(self):
        c = self.create_city()
        self.assertTrue(isinstance(c, City))
        self.assertEqual(c.__str__(), c.name)

    def create_airline(self, name="test"):
    	return Airline.objects.create(name=name)

    def test_airline_creation(self):
    	a = self.create_airline()
    	self.assertTrue(isinstance(a, Airline))
    	self.assertEqual(a.__str__(), a.name)

