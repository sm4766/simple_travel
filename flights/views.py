from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
#from django.core.urlresolvers import reverse
from time import sleep
from .models import City, Route, Airline, Flight, PaymentInfo


def index(request):
	cities = City.objects.all()
	context = {
		'cities': cities,
	}
	return render(request, 'flights/index.html', context)

def reserve(request):
	if request.method == 'POST':
		from_city = get_object_or_404(City, name=request.POST['from_city'])
		to_city = get_object_or_404(City, name=request.POST['to_city'])
		#to_city = request.POST['to_city']

		#routes = get_object_or_404(Route, from_city__exact=from_city, to_city__exact=to_city)
		routes = get_list_or_404(Route, from_city=from_city, to_city=to_city)
		flights = []
		for route in routes:
			print route
			flights.extend(get_list_or_404(Flight, route=route))
		print flights
		context = {
			'route': route,
			'flights': flights,
		}
		print context
		sleep(5)
		return render(request, 'flights/reserve.html', context)
	else:
		return HttpResponseRedirect('/')