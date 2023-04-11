from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.task1.models import Vacancy, Company, Resume


class GetCountAPIView(APIView):

    def get(self, request):
        vacancy = Vacancy.objects.count()
        company = Company.objects.count()
        resume = Resume.objects.count()

        get_count = {
            'vacancy_count': vacancy,
            'company_count': company,
            'resume_count': resume
        }
        return Response(get_count, status.HTTP_200_OK)

