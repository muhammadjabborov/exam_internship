from django.db import models
from django.db.models import CharField, ImageField, ForeignKey, CASCADE, TextField, DecimalField, Avg

from apps.task1.models import BaseModel


class Brand(BaseModel):
    title = CharField(max_length=255)
    logo = ImageField(upload_to='%Y/%m/%d')

    def __str__(self):
        return self.title


class Car(BaseModel):
    brand = ForeignKey(Brand, CASCADE)
    name = CharField(max_length=255)

    def __str__(self):
        return self.name


class Announcement(BaseModel):
    car = ForeignKey(Car, CASCADE)
    image = ImageField(upload_to='%Y/%m/%d')
    title = CharField(max_length=255)
    description = TextField()
    price = DecimalField(decimal_places=2, max_digits=6)

    def __str__(self):
        return self.title

    @property
    def get_avg_price(self):
        avg_price = self.car.announcement_set.aggregate(Avg('price')).get('price__avg')
        return avg_price

    @property
    def get_percentage_price(self):
        percentage_price = ((self.price * 100) / self.get_avg_price)
        return percentage_price
