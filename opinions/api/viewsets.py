from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from opinions.api.serializers import OpinionSerializer
from opinions.models import Opinion


class OpinionViewSet(viewsets.ModelViewSet):
    queryset = Opinion.objects.all()
    serializer_class = OpinionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
