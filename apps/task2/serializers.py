from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

from apps.task2.models import Feedback, Product, Service


class UserDataSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name')


class ListFeedbackModelSerializer(ModelSerializer):
    user = UserDataSerializer(read_only=True)

    class Meta:
        model = Feedback
        fields = (
            'id', 'user', 'description', 'greeting',
            'greeting_stats', 'get_count_feedback'
        )


class CreateFeedbackModelSerializer(ModelSerializer):
    class Meta:
        model = Feedback
        fields = ('id', 'user', 'greeting', 'description', 'service')


class ListProductModelSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'discount')


class DetailServiceModelSerializer(ModelSerializer):
    get_products = ListProductModelSerializer(many=True, source='product_set')
    get_feedbacks = ListFeedbackModelSerializer(many=True, source='feedback_set')

    class Meta:
        model = Service
        fields = ('id', 'logo', 'title', 'get_products', 'get_feedbacks', 'avg_rating')


class DestroyFeedbackModelSerializer(ModelSerializer):
    class Meta:
        model = Feedback
        fields = ('id', 'user')
