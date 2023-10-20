from django.db.models import *

class Guest(Model):
    first_name = CharField(max_length=250)
    last_name = CharField(max_length=250)
    email = EmailField()
    phone_number = CharField(max_length=515)