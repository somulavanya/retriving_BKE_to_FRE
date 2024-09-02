from django.db import models
import datetime
import django.utils.timezone

# Create your models here.
class Flights(models.Model):
    flight_number=models.IntegerField(primary_key=True)
    airline_name=models.CharField(max_length=50)
    No_of_seats_available=models.IntegerField()
    source=models.CharField(max_length=50)
    source_code=models.CharField(max_length=5)
    destination=models.CharField(max_length=100)
    destination_code=models.CharField(max_length=5)
    arraival_time=models.DateTimeField()
    depature_time=models.DateField()
    def __str__(self):
        return self.destination

class passenger(models.Model):
    pnr=models.CharField(max_length=50,primary_key=True)
    First_name=models.CharField(max_length=50)
    Last_name=models.CharField(max_length=50)
    dob=models.DateField()
    gender=models.CharField(max_length=7)
    nationality=models.CharField(max_length=10)
    flight_number=models.ForeignKey(Flights,on_delete=models.CASCADE)
    checkin_status=models.BooleanField(default=0)
    cleared_security_status=models.IntegerField(default=0)

