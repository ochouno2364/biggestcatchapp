from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Trip, Fish
from .forms import LocationForm
from django.contrib.auth.views import LoginView



# Create your views here.


class Home(LoginView):
    template_name = 'home.html'


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
    fish = Fish.objects.all()
    fish_trip_doesnt_have = Fish.objects.exclude(id__in = trip.fish.all().values_list('id'))
    location_form = LocationForm()
    return render(request, 'trips/tripdetail.html', {
        'trip': trip,
        'location_form': location_form,
        'fish': fish_trip_doesnt_have
        })


class TripCreate(CreateView):
    model = Trip
    fields = ['name', 'date', 'gear']

class TripUpdate(UpdateView):
    model = Trip
    fields = '__all__'

class TripDelete(DeleteView):
    model = Trip
    success_url = '/trips/'
    

def add_location(request, trip_id):
    form = LocationForm(request.POST)
    if form.is_valid():
        new_location = form.save(commit=False)
        new_location.trip_id = trip_id
        new_location.save()
    return redirect('trip-detail', trip_id=trip_id )


class FishCreate(CreateView):
    model = Fish
    fields = '__all__'

class FishList(ListView):
    model = Fish

class FishDetail(DetailView):
    model = Fish

class FishUpdate(UpdateView):
    model = Fish
    fields = ['color', 'weight', 'bait']

class FishDelete(DeleteView):
    model = Fish
    success_url = '/fish/'
    

def associate_fish(request, trip_id, fish_id):
    Trip.objects.get(id=trip_id).fish.add(fish_id)
    return redirect('trip-detail', trip_id=trip_id)


def remove_fish(request, trip_id, fish_id):
    trip = Trip.objects.get(id=trip_id)
    fish = Fish.objects.get(id=fish_id)
    trip.fish.remove(fish)
    
    return redirect('trip-detail', trip_id=trip.id)
