from django.contrib import admin

from .models import City, Route, Airline, Flight, PaymentInfo

admin.site.register(City)
admin.site.register(Route)
admin.site.register(Airline)
admin.site.register(Flight)
admin.site.register(PaymentInfo)
