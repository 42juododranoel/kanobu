import pytest

from opinions.models import Opinion

pytestmark = [pytest.mark.django_db]


def test_list_publications(api_client, publication):
    response = api_client.get('/api/publications/')

    assert response.status_code == 200
    assert response.json()[0]['id'] == publication.id


def test_retrieve_publication(api_client, publication):
    response = api_client.get(f'/api/publications/{publication.id}/')

    assert response.status_code == 200
    assert response.json()['id'] == publication.id


@pytest.mark.parametrize(
    'count_attribute, expected_value',
    [
        ['opinion_count', 1],
        ['like_count', 1],
        ['dislike_count', 0],
    ]
)
def test_list_counts_opinions(api_client, publication, create_opinion, count_attribute, expected_value):
    create_opinion(content_object=publication, category=Opinion.CATEGORY_LIKE)

    response = api_client.get('/api/publications/')

    assert response.json()[0][count_attribute] == expected_value


@pytest.mark.parametrize(
    'count_attribute, expected_value',
    [
        ['opinion_count', 1],
        ['like_count', 0],
        ['dislike_count', 1],
    ]
)
def test_retrieve_counts_opinions(api_client, publication, create_opinion, count_attribute, expected_value):
    create_opinion(content_object=publication, category=Opinion.CATEGORY_DISLIKE)

    response = api_client.get(f'/api/publications/{publication.id}/')

    assert response.json()[count_attribute] == expected_value
