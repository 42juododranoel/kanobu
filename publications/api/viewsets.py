from rest_framework import viewsets, mixins

from publications.models import Publication
from publications.api.serializers import PublicationSerializer


class PublicationViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
