from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.db.models import Model, DateTimeField, CharField, TextField, IntegerField, TextChoices, ImageField, \
    FileField, ForeignKey, CASCADE


class BaseModel(Model):
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class TypeChoices(TextChoices):
    full_time = ('Polnaya stavka', 'FT')
    part_time = ('Pol stavka', 'PT')


class Vacancy(BaseModel):
    title = CharField(max_length=255)
    experience = IntegerField()
    description = TextField()
    type = CharField(max_length=25, choices=TypeChoices.choices, default=TypeChoices.full_time)
    tags = ArrayField(CharField(max_length=25))


class Company(BaseModel):
    title = CharField(max_length=255)
    description = TextField()
    logo = ImageField(upload_to='%Y/%m/%d')


class Resume(BaseModel):
    file = FileField(upload_to='%Y/%m/%d')
    vacancy = ForeignKey('task1.Vacancy', CASCADE)
