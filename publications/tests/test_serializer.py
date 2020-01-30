from freezegun import freeze_time
from mixer.backend.django import mixer
import pytest

from publications.api.serializers import PublicationSerializer
from publications.models import Publication


@pytest.fixture
def publication():
    with freeze_time('2001-01-01 12:00'):
        return mixer.blend(Publication)


@pytest.mark.django_db
def test_serialize_publication(publication):
    serializer = PublicationSerializer(publication)
    assert serializer.data  # No errors
