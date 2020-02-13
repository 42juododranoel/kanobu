import pytest
from django.contrib.contenttypes.models import ContentType
from django.db.utils import IntegrityError

from opinions.models import Opinion

pytestmark = [pytest.mark.django_db]


def test_category_like_by_default(opinion):
    assert opinion.is_like


@pytest.mark.parametrize(
    'category',
    [
        'like',
        'dislike',
    ]
)
def test_category_properties(opinion, category):
    opinion.update(category=getattr(Opinion, f'CATEGORY_{category.upper()}'))

    assert getattr(opinion, f'is_{category}')


def test_generic_foreign_key_to_comment(opinion, comment):
    opinion.update(content_object=comment)

    assert opinion.content_type == ContentType.objects.get_for_model(comment)
    assert opinion.object_id == comment.id


def test_generic_foreign_key_to_publication(opinion, publication):
    opinion.update(content_object=publication)

    assert opinion.content_type == ContentType.objects.get_for_model(publication)
    assert opinion.object_id == publication.id


def test_cant_create_two_opinions_with_same_publication(publication, create_opinion):
    opinion = create_opinion(content_object=publication)

    with pytest.raises(IntegrityError):
        create_opinion(content_object=publication, owner=opinion.owner)


def test_cant_create_two_opinions_with_same_comment(comment, create_opinion):
    opinion = create_opinion(content_object=comment)

    with pytest.raises(IntegrityError):
        create_opinion(content_object=comment, owner=opinion.owner)
