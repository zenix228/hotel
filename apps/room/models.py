from django.db.models import *

from apps.hotel.models import Hotel

class Room(Model):
    hotel = ForeignKey(Hotel, on_delete=CASCADE)
    number = IntegerField()
    capacity = IntegerField()
    price_per_night = IntegerField()