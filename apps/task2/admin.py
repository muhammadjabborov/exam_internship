from django.contrib import admin

from apps.task2.models import Feedback, Product, Service

admin.site.register(Feedback)
admin.site.register(Product)
admin.site.register(Service)