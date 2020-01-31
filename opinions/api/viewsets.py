from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from opinions.api.serializers import OpinionSerializer
from opinions.models import Opinion


class OpinionViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Opinion.objects.all()
    serializer_class = OpinionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
