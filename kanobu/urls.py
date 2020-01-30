from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from comments.api.viewsets import CommentViewSet
from publications.api.viewsets import PublicationViewSet


router = routers.DefaultRouter()
router.register('publications', PublicationViewSet)
router.register('comments', CommentViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
