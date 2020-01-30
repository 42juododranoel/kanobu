import pytest

from opinions.api.serializers import OpinionSerializer


@pytest.mark.django_db
def test_serialize_opinion(opinion):
    serializer = OpinionSerializer(opinion)
    serializer.data  # No errors
