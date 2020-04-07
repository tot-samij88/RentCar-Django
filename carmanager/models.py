from django.db import models
from datetime import datetime


class CarManager(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/%Y%m%d')
    position = models.CharField(max_length=100,blank=True)
    desription = models.TextField(blank=True)
    phone1 = models.CharField(max_length=20,blank=True)
    phone2 = models.CharField(max_length=20,blank=True)
    phone3 = models.CharField(max_length=20,blank=True)
    tg = models.CharField(max_length=100,blank=True)
    is_published = models.BooleanField(default=True)
    email = models.EmailField(max_length=254)
    age_date = models.DateField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
