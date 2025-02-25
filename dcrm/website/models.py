from django.db import models
from django.contrib.auth.models import User
# Create your models here.


#Ticket model


class Ticket(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)  # User relationship

    #Quantity of people going on one ticket. No Adult/Child difference
    Quantity = models.PositiveIntegerField()

    #Time-related fields
    Arrival_Time = models.TimeField()
    Departure_Time = models.TimeField()
    Booking_Date = models.DateField()


    Price = models.DecimalField(max_digits=10, decimal_places=2,default=0) # NN,NNN,NNN.NN   10 digits. 2dp.