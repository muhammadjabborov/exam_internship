from django.contrib.auth.models import User
from django.core import serializers
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import ImageField, CharField, FloatField, ForeignKey, CASCADE, TextField, Avg, Count
from django.db.models.functions import Trunc

from apps.task1.models import BaseModel


class Service(BaseModel):
    logo = ImageField(upload_to='%Y/%m/%d')
    title = CharField(max_length=255)

    @property
    def avg_rating(self):
        return self.feedback_set.all().aggregate(Avg('greeting'))['greeting__avg']


class Product(BaseModel):
    title = CharField(max_length=255)
    service = ForeignKey(Service, CASCADE)
    discount = FloatField()


class Feedback(BaseModel):
    user = ForeignKey(User, CASCADE)
    service = ForeignKey(Service, CASCADE)
    description = TextField()
    greeting = FloatField(validators=[
        MaxValueValidator(5, 'The max should be 5'),
        MinValueValidator(1, 'The min should be 1')
    ])

    def __str__(self):
        return self.user.first_name

    @property
    def greeting_stats(self):
        feedback_stats = Feedback.objects.filter(greeting__gte=1, greeting__lte=5).values('greeting').annotate(
            rating_count=Count('greeting')
        ).order_by('greeting')

        stats_dict = {}
        for stat in feedback_stats:
            stats_dict[stat['greeting']] = stat['rating_count']

        return stats_dict

    @property
    def get_count_feedback(self):
        feedback_count = Feedback.objects.count()
        return feedback_count
