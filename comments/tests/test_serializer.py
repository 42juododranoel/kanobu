import pytest

from comments.api.serializers import CommentSerializer


@pytest.mark.django_db
def test_serialize_comment(comment):
    serializer = CommentSerializer(comment)
    assert serializer.data  # No errors
