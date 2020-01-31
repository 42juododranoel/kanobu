from django.db.models import Count, Q
from rest_framework import viewsets, mixins

from opinions.models import Opinion
from publications.models import Publication
from publications.api.serializers import PublicationSerializer


class PublicationViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Publication.objects.annotate(
        opinion_count=Count('opinions'),
        like_count=Count('opinions', filter=Q(opinions__category=Opinion.CATEGORY_LIKE)),
        dislike_count=Count('opinions', filter=Q(opinions__category=Opinion.CATEGORY_DISLIKE)),
    )
    serializer_class = PublicationSerializer
