import pytest
from django.utils import timezone
from freezegun import freeze_time

from publications.models import Publication

pytestmark = [pytest.mark.django_db]


@pytest.mark.parametrize(
    'attribute',
    [
        'title',
        'content',
        'author',
    ]
)
def test_attributes(publication, attribute):
    assert getattr(publication, attribute)


def test_published_at_none_by_default(publication):
    assert publication.published_at is None


def test_category_article_by_default(publication):
    assert publication.is_article


@pytest.mark.parametrize(
    'category',
    [
        'article',
        'news',
    ]
)
def test_category_properties(publication, category):
    publication.update(category=getattr(Publication, f'CATEGORY_{category.upper()}'))
    assert getattr(publication, f'is_{category}')


@freeze_time('2001-01-01 12:00')  # Same as in fixture
def test_created_at_auto_now_add(publication):
    assert publication.created_at == timezone.now()


def test_has_opinion_relation(publication, publication_opinion):
    publication_opinion.update(object_id=publication.id)
    assert publication_opinion in publication.opinions.all()
