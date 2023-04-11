from django.shortcuts import render
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.parsers import MultiPartParser, FormParser

from apps.task2.models import Feedback, Product, Service
from apps.task2.serializers import ListFeedbackModelSerializer, CreateFeedbackModelSerializer, \
    ListProductModelSerializer, DetailServiceModelSerializer, DestroyFeedbackModelSerializer


class ListFeedbackAPIView(ListAPIView):
    queryset = Feedback.objects.order_by('-created_at')
    serializer_class = ListFeedbackModelSerializer


class CreateFeedbackAPIView(CreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = CreateFeedbackModelSerializer

    def perform_create(self, serializer):
        user_id = self.request.data.get('user')
        service_id = self.request.data.get('service')
        existing_feedback = Feedback.objects.filter(user=user_id, service=service_id).exists()

        if existing_feedback:
            raise PermissionDenied("You can only write one feedback per product.")

        serializer.save(user=user_id, service=service_id)


class DeleteFeedbackAPIView(DestroyAPIView):
    queryset = Feedback.objects.all()
    lookup_field = 'pk'

    def get_object(self):
        feedback = super().get_object()
        user = self.request.user
        if feedback.user != user:
            raise PermissionDenied("You don't have permission to delete this feedback.")
        return feedback


class DetailServiceAPIView(RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = DetailServiceModelSerializer
    lookup_field = 'pk'
    parser_classes = (FormParser, MultiPartParser)
