from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView

from apps.task3.models import Brand, Car, Announcement
from apps.task3.serializers import ListBrandModelSerializer, ListCarModelSerializer, AnnouncementDetailModelSerializer


class ListBrandAPIView(ListAPIView):
    queryset = Brand.objects.order_by('-created_at')
    serializer_class = ListBrandModelSerializer


class ListCarAPIView(ListAPIView):
    queryset = Car.objects.order_by('-created_at')
    serializer_class = ListCarModelSerializer


class DetailAnnouncementAPIView(RetrieveAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementDetailModelSerializer
    lookup_field = 'pk'

