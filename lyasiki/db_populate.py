import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lyasiki.settings')
django.setup()

from lyasikservice.models import Station, Bike, Employee


def populate():
    station1 = Station.objects.create(name="Бомбей", location="вулиця Сергія Синенка, 69", capacity=20)
    station2 = Station.objects.create(name="Бабурка", location="вулиця Сорочинська, 22А", capacity=15)

    bike1 = Bike.objects.create(station=station1, model="Гірський велосипед Ardis", status="available", total_usage=0)
    bike2 = Bike.objects.create(station=station1, model="Міський велосипед Atlantic", status="available", total_usage=0)
    bike3 = Bike.objects.create(station=station1, model="Гірський велосипед Formula", status="available", total_usage=0)
    bike4 = Bike.objects.create(station=station1, model="Міський велосипед Crossride", status="available", total_usage=0)
    bike5 = Bike.objects.create(station=station1, model="Міський велосипед Kona Dew Deluxe", status="available", total_usage=0)
    bike6 = Bike.objects.create(station=station2, model="Гірський велосипед Ardis", status="available", total_usage=0)
    bike7 = Bike.objects.create(station=station2, model="Міський велосипед Atlantic", status="available", total_usage=0)
    bike8 = Bike.objects.create(station=station2, model="Гірський велосипед Formula", status="available", total_usage=0)
    bike9 = Bike.objects.create(station=station2, model="Міський велосипед Crossride", status="available", total_usage=0)
    bike10 = Bike.objects.create(station=station2, model="Міський велосипед Kona Dew Deluxe", status="available", total_usage=0)

    employee1 = Employee.objects.create(first_name="Ігор", last_name="Степанов", position="Менеджер")
    employee2 = Employee.objects.create(first_name="Володимир", last_name="Борисенко", position="Менеджер")


if __name__ == '__main__':
    print("Заповнюємо базу даних...")
    populate()
    print("Заповнення завершено.")