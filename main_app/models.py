from django.db import models
from django.urls import reverse

# Create your models here.
BODIES = (
    ('O', 'Ocean'),
    ('L', 'Lake'),
    ('R', 'River'),
    ('P', 'Pond'),
    ('C', 'Creek'),
)
WATERS = (
    ('F', 'Fresh Water'),
    ('S', 'Salt Water'),

)

WEATHER = (
    ('S', 'Sunny'),
    ('C', 'Cloudy'),
    ('R', 'Rainy'),
    ('T', 'Thunder'),
    ('W', 'Windy'),
    ('F', 'Foggy'),
)

class Trip(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField('Date Of Trip')
    gear = models.CharField(max_length=100)
    # fish = models.ManyToManyField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('trip-detail', kwargs={'trip_id': self.id})

class Location(models.Model):
    name = models.CharField(max_length=50)
    body = models.CharField(max_length=1, default=[0][0], choices=BODIES)
    water = models.CharField(max_length=1, default=[0][0], choices=WATERS)
    address = models.CharField(max_length=200)
    weather = models.CharField(max_length=20, default=[0][0], choices=WEATHER)

    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, default=[0][0])

    def __str__(self):
        return f"{self.name} {self.get_body_display()} at {self.address}"