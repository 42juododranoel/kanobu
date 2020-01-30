import pytest


@pytest.mark.django_db
def test_publication_list(api_client, publication):
    response = api_client.get('/api/publications/')
    assert response.json()[0]['id'] == 1


@pytest.mark.django_db
def test_publication_retrieve(api_client, publication):
    response = api_client.get('/api/publications/1/')
    assert response.json()['id'] == 1
