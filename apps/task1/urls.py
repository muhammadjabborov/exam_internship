from django.urls import path

from apps.task1.views import GetCountAPIView

urlpatterns = [
    path('count/', GetCountAPIView.as_view(), name='count')
]
