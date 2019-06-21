from django.db import models
from SpaceTravels import settings

# Create your models here.
class Flight(models.Model):
    departure_date = models.CharField(max_length=16)
    arrival_date =  models.CharField(max_length=16)
    seats_amount = models.IntegerField()
    ticket_price = models.DecimalField(max_digits=6, decimal_places=2)
    tourists = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
    
    def get_tourists_list(self):
        '''Getting list of all Tourists of actual flight'''
        return self.tourists.prefetch_related()

    def __str__(self):
        return "Departure: {},\n Arrival: {},\n Seats: {}\n, Ticket price: {}\n ".format(self.departure_date, self.arrival_date, self.seats_amount, self.ticket_price, self.tourists)