from django.db import models
from datetime import datetime


class Contacts(models.Model):
    cars = models.CharField(max_length=50)
    car_id = models.IntegerField()
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=20)
    message = models.TextField(blank=True)
    contact_date = models.DateField(default=datetime.now, blank=True)
    user_id = models.IntegerField(blank=True)

    def __str__(self):
        return self.name
