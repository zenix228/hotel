from django.db.models import *

class Hotel(Model):
    name = CharField(max_length=250)
    address = CharField(max_length=510)
    city = CharField(max_length=2651)
    country = CharField(max_length=250)
    rating = DecimalField()
