from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Trip



# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

# class Trip:
#     def __init__(self, name, date, gear, fish):
#         self.name = name
#         self.date = date
#         self.gear = gear
#         self.fish = fish

# # trips = [
# #     Trip('First Trip', 12-1-2011, 'openfaced reel', 'large mouth bass'),
# #     Trip('Best Trip', 2-1-2013, 'fake worm', 'small mouth bass'),
# #     Trip('Worse Trip', 11-1-2015, 'closed reel', 'perch'),
# #     Trip('last Trip', 8-1-2017, 'openfaced reel', 'catfish'),
# # ]

def trip_index(request):
    trips = Trip.objects.all()
    return render(request, 'trips/tripindex.html', {'trips': trips})


def trip_detail(request, trip_id):
    trip = Trip.objects.get(id=trip_id)
    return render(request, 'trips/tripdetail.html', {'trip': trip})


class TripCreate(CreateView):
    model = Trip
    fields = '__all__'

class TripUpdate(UpdateView):
    model = Trip
    fields = '__all__'

class TripDelete(DeleteView):
    model = Trip
    success_url = '/trips/'
    