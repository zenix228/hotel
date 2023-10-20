from django.db.models import *

from apps.room.models import Room
from apps.guest.models import Guest

class Booking(Model):
    room = ForeignKey(Room, on_delete=CASCADE)
    guest = ForeignKey(Guest, on_delete=CASCADE)
    check_in_date = DateField(auto_now_add=True)
    check_out_date = DateField()
    is_paid = BooleanField(default=False)
