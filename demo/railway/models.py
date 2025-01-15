import datetime
from django.db import models
from django.contrib.auth.models import User


class Station(models.Model):
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}, {self.place}"

class ClassTypes(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price per passenger

    def __str__(self):
        return self.name

class Train_data(models.Model):
    name = models.CharField(max_length=100)
    number=models.CharField(max_length=10,unique=True)
    source = models.ForeignKey(Station, related_name='source_trains', on_delete=models.CASCADE)
    destination = models.ForeignKey(Station, related_name='destination_trains', on_delete=models.CASCADE)
    departure_time = models.TimeField()
    arrival_time = models.TimeField()
    class_type = models.ManyToManyField(ClassTypes)  # Trains can have multiple class types (e.g., Sleeper, AC)
    departure_date = models.DateField(null=True, blank=True)


    def __str__(self):
        return self.name

    def duration(self):
        # Calculate duration between departure and arrival times
        dep = datetime.combine(datetime.today(), self.departure_time)
        arr = datetime.combine(datetime.today(), self.arrival_time)
        return arr - dep if arr > dep else (arr + datetime.timedelta(days=1)) - dep

    
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    train_number = models.CharField(max_length=10)
    departure_date = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    passengers = models.IntegerField()
    class_type = models.CharField(max_length=50)
    booking_date = models.DateTimeField(auto_now_add=True)




class Passenger(models.Model):
    age = models.CharField(max_length=3)
    seat_preference = models.CharField(max_length=10, choices=[('Window', 'Window'), ('Aisle', 'Aisle'), ('Middle', 'Middle')])
    passenger_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=15)
    departure = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    booking_date = models.DateTimeField(auto_now_add=True)  # Auto-set to current date on creation

    # Add the train field as a ForeignKey to Train
   
    def __str__(self):
        return self.passenger_name
