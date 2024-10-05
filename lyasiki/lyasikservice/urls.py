from django.urls import path
from . import views

urlpatterns = [
    path('bikes/', views.bike_list, name='bike_list'),
    path('stations/', views.station_list, name='station_list'),
    path('stations/<int:station_id>/bikes/', views.station_bikes, name='station_bikes'),
    path('bikes/add/', views.add_bike, name='add_bike'),
    path('rent/<int:bike_id>/', views.rent_bike, name='rent_bike'),
    path('bikes/<int:bike_id>/return/', views.return_bike, name='return_bike'),
    path('bikes/<int:bike_id>/details/', views.bike_details, name='bike_details'),
    path('delete/<int:bike_id>/', views.delete_bike, name='delete_bike'),
    path('bikes/<int:bike_id>/', views.bike_details, name='bike_detail'),
    path('bikes/<int:bike_id>/edit/', views.edit_bike, name='bike_edit'),
    path('bikes/<int:bike_id>/delete/', views.delete_bike, name='bike_delete'),
    path('about/', views.about, name='about'),
]