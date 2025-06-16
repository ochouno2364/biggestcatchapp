from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('trips/', views.trip_index, name='trip-index'),
    path('trips/<int:trip_id>/', views.trip_detail, name='trip-detail'),
    path('trips/create/', views.TripCreate.as_view(), name='trip-create'),
    path('trips/<int:pk>/update/', views.TripUpdate.as_view(), name='trip-update'),
    path('trips/<int:pk>/delete/', views.TripDelete.as_view(), name='trip-delete'),
    path('trip/<int:trip_id>/add-location/', views.add_location, name='add-location'),
    path('fish/create/', views.FishCreate.as_view(), name='fish-create'),
    path('fish/<int:pk>/', views.FishDetail.as_view(), name='fish-detail'),
    path('fish/', views.FishList.as_view(), name='fish-index'),
    path('fish/<int:pk>/update', views.FishUpdate.as_view(), name='fish-update'),
    path('fish/<int:pk>/delete', views.FishDelete.as_view(), name='fish-delete'),
    path('fish/<int:trip_id>/associate-fish/<int:fish_id>/', views.associate_fish, name='associate-fish'),
    path('trips/<int:trip_id>/remove-fish/<int:fish_id>/', views.remove_fish, name='remove-fish'),


]