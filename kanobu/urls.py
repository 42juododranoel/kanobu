from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from publications.api.viewsets import PublicationViewSet


router = routers.DefaultRouter()
router.register(r'publications', PublicationViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
