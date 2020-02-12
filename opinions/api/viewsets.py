from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from kanobu.utils.permissions import IsOwner, ReadOnly
from opinions.api.serializers import OpinionSerializer
from opinions.models import Opinion


class OpinionViewSet(viewsets.ModelViewSet):
    queryset = Opinion.objects.all()
    serializer_class = OpinionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly & (IsOwner | ReadOnly)]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
