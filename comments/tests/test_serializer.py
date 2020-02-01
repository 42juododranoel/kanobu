import pytest

from comments.api.serializers import CommentSerializer

pytestmark = [pytest.mark.django_db]


def test_serialize_comment(comment):
    serializer = CommentSerializer(comment)
    serializer.data  # No errors
