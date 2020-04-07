from django.db import models
from carmanager.models import CarManager

class CarsList(models.Model):
    carmanager = models.ForeignKey(CarManager, on_delete = models.DO_NOTHING)
    vendor = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    engine = models.CharField(max_length=20)
    fuel = models.DecimalField(max_digits=3, decimal_places=1)
    color = models.CharField(max_length=30)
    doors = models.IntegerField()
    seats = models.IntegerField()
    minimum_age = models.IntegerField()
    price = models.IntegerField()
    transmision = models.CharField(max_length=30,blank=True)
    rating = models.IntegerField()
    is_published = models.BooleanField(default=True)
    photo_main = models.ImageField(upload_to='photo_car/main',blank=True)
    photo_1 = models.ImageField(upload_to='photo_car/main/other',blank=True)
    photo_2 = models.ImageField(upload_to='photo_car/main/other',blank=True)
    photo_3 = models.ImageField(upload_to='photo_car/main/other',blank=True)

    def __str__(self):
        return self.vendor

