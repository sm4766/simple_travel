from __future__ import unicode_literals

from django.db import models


class City(models.Model):
	timestamp = models.DateTimeField('timestamp', auto_now_add=True)
	name = models.CharField('city name', max_length=128, unique=True)

	def __str__(self):
		return self.name


class Route(models.Model):
	timestamp = models.DateTimeField('timestamp', auto_now_add=True)
	from_city = models.ForeignKey(City, on_delete=models.CASCADE)
	to_city = models.ForeignKey(City, related_name='to_city_route', on_delete=models.CASCADE)

	def __str__(self):
		return self.from_city.name + " -> " + self.to_city.name


class Airline(models.Model):
	timestamp = models.DateTimeField('timestamp', auto_now_add=True)
	name = models.CharField('airline name', max_length=128, unique=True)

	def __str__(self):
		return self.name

class Flight(models.Model):
	timestamp = models.DateTimeField('timestamp', auto_now_add=True)
	flight_number = models.IntegerField('flight number', unique=False)
	airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
	route = models.ForeignKey(Route, on_delete=models.CASCADE)
	depart = models.DateTimeField('departure time')
	arrive = models.DateTimeField('arrival time')
	price = models.DecimalField('price', decimal_places=2, max_digits=8)

	def __str__(self):
		return str(self.flight_number)


class PaymentInfo(models.Model):
	CARD_TYPES = (
		('VISA', 'VISA'),
		('MC', 'MasterCard'),
	)
	timestamp = models.DateTimeField('timestamp', auto_now_add=True)
	name = models.CharField('name', max_length=128)
	address = models.CharField('address', max_length=128)
	city = models.CharField('city', max_length=128)
	state = models.CharField('state', max_length=2)
	zip_code = models.IntegerField('zip code')
	card_type = models.CharField('card type', max_length=16, choices=CARD_TYPES, default='VISA')
	card_number = models.IntegerField('card number')
	name_on_card = models.CharField('name on card', max_length=128)

	def __str__(self):
		return self.name + ", " + self.card_type


# class User(models.Model):
# 	name = models.CharField('username', max_length=32)
# 	password = models.CharField('password', max_length=128)

# 	def __str__(self):
# 		return self.name
