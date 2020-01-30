from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from opinions.models import Opinion
from opinions.api.serializers import OpinionSerializer


class OpinionViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Opinion.objects.all()
    serializer_class = OpinionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
