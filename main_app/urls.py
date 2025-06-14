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

]