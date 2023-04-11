from django.urls import path

from apps.task2.views import ListFeedbackAPIView, CreateFeedbackAPIView, DetailServiceAPIView, DeleteFeedbackAPIView

urlpatterns = [
    path('list/feedbacks/', ListFeedbackAPIView.as_view(), name='list_feedback'),
    path('create/feedback/', CreateFeedbackAPIView.as_view(), name='create_feedback'),
    path('detail/service/<int:pk>/', DetailServiceAPIView.as_view(), name='detail_service'),
    path('delete/feedback/<int:pk>/', DeleteFeedbackAPIView.as_view(), name='delete_feedback')

]
