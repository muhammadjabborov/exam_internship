from django.urls import path

from apps.task3.views import ListBrandAPIView, ListCarAPIView, DetailAnnouncementAPIView

urlpatterns = [
    path('list/brand/', ListBrandAPIView.as_view(), name='list_brand'),
    path('list/cars/', ListCarAPIView.as_view(), name='list_car'),
    path('detail/announcement/<int:pk>/', DetailAnnouncementAPIView.as_view(), name='announcement')
]
