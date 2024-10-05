from django.db import models
from django.utils import timezone


class Station(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name


class Bike(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('in_use', 'In Use'),
        ('maintenance', 'Under Maintenance'),
    ]

    station = models.ForeignKey(Station, on_delete=models.SET_NULL, null=True, related_name='bikes')
    model = models.CharField(max_length=100)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='available')
    total_usage = models.IntegerField(default=0)

    def __str__(self):
        return self.model


class Rental(models.Model):
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(null=True, blank=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def calculate_cost(self):
        if self.end_time:
            duration = (self.end_time - self.start_time).total_seconds() / 3600
            rate_per_hour = 10.00  # Ціна за годину оренди
            self.total_cost = round(duration * rate_per_hour, 2)
        return self.total_cost

    def __str__(self):
        return f'{self.user_name} - {self.bike}'


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
