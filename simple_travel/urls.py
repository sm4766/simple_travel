"""simple_travel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers, serializers, viewsets

from flights.models import City, Airline, Route, Flight, PaymentInfo
from flights import views


class CitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = City
        fields = ('name',)


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class AirlineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Airline
        fields = ('name',)


class AirlineViewSet(viewsets.ModelViewSet):
    queryset = Airline.objects.all()
    serializer_class = AirlineSerializer


class RouteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Route
        fields = ('from_city', 'to_city')


class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer


class FlightSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Flight
        fields = ('flight_number', 'airline', 'route', 'depart', 'arrive', 'price')


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class PaymentInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PaymentInfo
        fields = ('name', 'address', 'city', 'state', 'zip_code', 'card_type', 'card_number', 'name_on_card')


class PaymentInfoViewSet(viewsets.ModelViewSet):
    queryset = PaymentInfo.objects.all()
    serializer_class = PaymentInfoSerializer


router = routers.DefaultRouter()
router.register(r'api/cities', CityViewSet)
router.register(r'api/airlines', AirlineViewSet)
router.register(r'api/routes', RouteViewSet)
router.register(r'api/flights', FlightViewSet)
router.register(r'api/payment_infos', PaymentInfoViewSet)


app_name = 'flights'
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^reserve/', views.reserve, name='reserve'),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
