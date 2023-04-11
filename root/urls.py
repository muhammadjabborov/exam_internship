from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from root import settings

schema_view = get_schema_view(
    openapi.Info(
        title="Task API",
        default_version='v1',
        description="Backend API for Task",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('jobhunt/', include('apps.task1.urls'), name='jobhunt'),
    path('befit/pro/', include('apps.task2.urls'), name='befit'),
    path('auto/', include('apps.task3.urls'), name='auto')

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + \
               static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
