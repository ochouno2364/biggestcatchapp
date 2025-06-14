from django.db import models
from django.urls import reverse

# Create your models here.

class Trip(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()
    gear = models.CharField(max_length=100)
    # fish = models.ManyToManyField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('trip-detail', kwargs={'trip_id': self.id})

