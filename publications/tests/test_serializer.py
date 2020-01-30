import pytest

from publications.api.serializers import PublicationSerializer


@pytest.mark.django_db
def test_serialize_publication(publication):
    serializer = PublicationSerializer(publication)
    serializer.data  # No errors
