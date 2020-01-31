import pytest
from django.db.utils import IntegrityError


@pytest.mark.django_db
@pytest.mark.parametrize(
    'attribute',
    [
        'text',
        'publication',
        'owner',
    ]
)
def test_not_none_attributes(comment, attribute):
    with pytest.raises(IntegrityError):
        comment.update(**{attribute: None})
