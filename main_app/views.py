from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Trip, Fish
from .forms import LocationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin




# Create your views here.
def signup(request):
    error_message = ''
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('trip-index')
        else:
            error_message = 'Invalid sign-up try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)


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

@login_required
def trip_index(request):
    trips = Trip.objects.filter(user=request.user)
    return render(request, 'trips/tripindex.html', {'trips': trips})

@login_required
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


class TripCreate(LoginRequiredMixin, CreateView):
    model = Trip
    fields = ['name', 'date', 'gear']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

class TripUpdate(LoginRequiredMixin, UpdateView):
    model = Trip
    fields = '__all__'


class TripDelete(LoginRequiredMixin, DeleteView):
    model = Trip
    success_url = '/trips/'
    
@login_required
def add_location(request, trip_id):
    form = LocationForm(request.POST)
    if form.is_valid():
        new_location = form.save(commit=False)
        new_location.trip_id = trip_id
        new_location.save()
    return redirect('trip-detail', trip_id=trip_id )


class FishCreate(LoginRequiredMixin, CreateView):
    model = Fish
    fields = '__all__'


class FishList(LoginRequiredMixin, ListView):
    model = Fish


class FishDetail(LoginRequiredMixin, DetailView):
    model = Fish


class FishUpdate(LoginRequiredMixin, UpdateView):
    model = Fish
    fields = ['color', 'weight', 'bait']


class FishDelete(LoginRequiredMixin, DeleteView):
    model = Fish
    success_url = '/fish/'
    
@login_required
def associate_fish(request, trip_id, fish_id):
    Trip.objects.get(id=trip_id).fish.add(fish_id)
    return redirect('trip-detail', trip_id=trip_id)

@login_required
def remove_fish(request, trip_id, fish_id):
    trip = Trip.objects.get(id=trip_id)
    fish = Fish.objects.get(id=fish_id)
    trip.fish.remove(fish)
    
    return redirect('trip-detail', trip_id=trip.id)
