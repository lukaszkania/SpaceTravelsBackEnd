from django.db import models
from django.contrib.auth.models import AbstractUser
from .choices import SEX_CHOICES
from flights.models import Flight


# Create your models here.
class Tourist(AbstractUser):
    '''Our User model, that inherit from django build in AbstractUser'''
    sex = models.CharField(max_length=8, default='Female') # Creating new field that will store user sex
    country = models.CharField(max_length=50)  
    email = models.EmailField(unique=True) # AbstractUser have email field, but is not required, so We overwrite it and make it required and unique so only one tourist can be assigned to only one email
    first_name = models.CharField(max_length=50) # Same as above
    last_name = models.CharField(max_length=50) # Same as above
    birth_date = models.CharField(max_length=20)
    notes = models.TextField(max_length=1000, default="", blank=True)
    flights = models.ManyToManyField(Flight, blank=True)

    def get_flights(self):
        '''Getting list of all Tourist future and past flights'''
        return self.flight_set.prefetch_related()

    def __str__(self):
        return self.first_name + " " + self.last_name
