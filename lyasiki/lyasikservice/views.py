from django.shortcuts import render, get_object_or_404, redirect
from .models import Bike, Station, Rental, Employee
from .forms import BikeForm
from django.utils import timezone


def home(request):
    employees = Employee.objects.all()
    return render(request, 'home.html', {'employees': employees})


def about(request):
    return render(request, 'about.html')


def bike_list(request):
    bikes = Bike.objects.all()
    return render(request, 'bikes/lyasik_list.html', {'bikes': bikes})


def station_list(request):
    stations = Station.objects.all()
    return render(request, 'stations/station_list.html', {'stations': stations})


def station_bikes(request, station_id):
    station = get_object_or_404(Station, id=station_id)
    bikes = station.bikes.filter(status='available')
    return render(request, 'bikes/station_lyasiki.html', {'station': station, 'bikes': bikes})


def add_bike(request):
    if request.method == 'POST':
        form = BikeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bike_list')
    else:
        form = BikeForm()
    return render(request, 'bikes/add_bike.html', {'form': form})


def delete_bike(request, bike_id):
    bike = get_object_or_404(Bike, id=bike_id)
    if request.method == 'POST':
        bike.delete()
        return redirect('bike_list')
    return render(request, 'bikes/delete_bike.html', {'bike': bike})


def rent_bike(request, bike_id):
    bike = get_object_or_404(Bike, id=bike_id)

    if request.method == 'POST':
        user_name = request.POST.get('user_name')

        if user_name:
            # Створюємо оренду
            rental = Rental.objects.create(
                bike=bike,
                user_name=user_name,
                start_time=timezone.now()
            )
            # Оновлюємо статус велосипеда
            bike.status = 'in_use'
            bike.save()

            return render(request, 'bikes/rent_bike.html', {'rental': rental, 'bike': bike})
        else:
            error_message = "Будь ласка, введіть ваше ім'я."
            return render(request, 'bikes/rent_bike.html', {'bike': bike, 'error_message': error_message})
    return render(request, 'bikes/rent_bike.html', {'bike': bike})


def return_bike(request, bike_id):
    # Отримуємо велосипед за ID
    bike = get_object_or_404(Bike, id=bike_id)

    # Отримуємо останню оренду для цього велосипеда
    rental = Rental.objects.filter(bike=bike, end_time__isnull=True).first()

    if request.method == 'POST':
        if rental:
            # Встановлюємо дату повернення
            rental.end_time = timezone.now()
            rental.calculate_cost()  # Розраховуємо вартість оренди
            rental.save()

            # Оновлюємо статус велосипеда
            bike.status = 'available'
            bike.total_usage += 1
            bike.save()

        # Переадресовуємо на сторінку підтвердження з відображенням вартості оренди
        return render(request, 'bikes/return_bike.html', {'rental': rental})

    return render(request, 'bikes/return_bike.html', {'rental': rental})


def edit_bike(request, bike_id):
    bike = get_object_or_404(Bike, id=bike_id)

    if request.method == 'POST':
        form = BikeForm(request.POST, instance=bike)
        if form.is_valid():
            form.save()
            return redirect('bike_list')
    else:
        form = BikeForm(instance=bike)
    return render(request, 'bikes/edit_bike.html', {'form': form, 'bike': bike})


def bike_details(request, bike_id):
    bike = get_object_or_404(Bike, id=bike_id)
    rentals = Rental.objects.filter(bike=bike).order_by('-start_time')
    return render(request, 'bikes/bike_details.html', {'bike': bike, 'rentals': rentals})