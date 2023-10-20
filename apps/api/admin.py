from django.contrib.admin import *

from apps.hotel.models import Hotel
from apps.room.models import Room
from apps.booking.models import Booking
from apps.guest.models import Guest

@register(Hotel)
class HotelAdmin(ModelAdmin):

    list_display = ('id', 'name', 'city', 'rating')
    list_display_links = ('id', 'name', 'city', 'rating')

@register(Room)
class RoomAdmin(ModelAdmin):

    list_display = ('id', 'hotel', 'number', 'capacity', 'price_per_night')
    list_display_links = ('id', 'hotel', 'number', 'capacity', 'price_per_night')

@register(Booking)
class BookingAdmin(ModelAdmin):

    list_display = ('id', 'room', 'guest', 'check_in_date', 'is_paid')
    list_display_links = ('id', 'room', 'guest', 'check_in_date', 'is_paid')

register(Guest)
class GuestAdmin(ModelAdmin):

    list_display = ('id', 'first_name', 'last_name', 'email')
    list_display_links = ('id', 'first_name', 'last_name', 'email')