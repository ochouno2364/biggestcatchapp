from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('trips/', views.trip_index, name='trip-index'),
    path('trips/<int:trip_id>/', views.trip_detail, name='trip-detail'),

]