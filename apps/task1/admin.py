from django.contrib import admin

from apps.task1.models import Resume, Vacancy, Company

admin.site.register(Vacancy)
admin.site.register(Company)
admin.site.register(Resume)
