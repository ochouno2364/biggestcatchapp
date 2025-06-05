from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

class Trip:
    def __init__(self, name, date, gear, fish):
        self.name = name
        self.date = date
        self.gear = gear
        self.fish = fish

trips = [
    Trip('First Trip', 12-1-2011, 'openfaced reel', 'large mouth bass'),
    Trip('Best Trip', 2-1-2013, 'fake worm', 'small mouth bass'),
    Trip('Worse Trip', 11-1-2015, 'closed reel', 'perch'),
    Trip('last Trip', 8-1-2017, 'openfaced reel', 'catfish'),
]

def trip_index(request):
    return render(request, 'trips/tripindex.html', {'trips': trips})