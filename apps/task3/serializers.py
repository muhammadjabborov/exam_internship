from rest_framework.serializers import ModelSerializer

from apps.task3.models import Brand, Car, Announcement


class ListBrandModelSerializer(ModelSerializer):
    class Meta:
        model = Brand
        fields = ('id', 'title', 'logo')


class ListCarModelSerializer(ModelSerializer):
    brand = ListBrandModelSerializer(read_only=True)

    class Meta:
        model = Car
        fields = ('id', 'brand', 'name')


class AnnouncementDetailModelSerializer(ModelSerializer):
    car = ListCarModelSerializer(read_only=True)

    class Meta:
        model = Announcement
        fields = (
            'id', 'title', 'car', 'image', 'description',
            'price', 'get_avg_price', 'get_percentage_price'
        )
