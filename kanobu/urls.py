from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from comments.api.viewsets import CommentViewSet
from opinions.api.viewsets import OpinionViewSet
from publications.api.viewsets import PublicationViewSet

router = routers.DefaultRouter()
router.register('publications', PublicationViewSet)
router.register('comments', CommentViewSet)
router.register('opinions', OpinionViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
