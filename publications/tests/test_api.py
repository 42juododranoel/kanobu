import pytest
from rest_framework.test import APIClient


@pytest.fixture
def client():
    return APIClient()


@pytest.mark.django_db
def test_publication_list(client, publication):
    response = client.get('/api/publications/')
    assert response.json()[0]['id'] == 1


@pytest.mark.django_db
def test_publication_retrieve(client, publication):
    response = client.get('/api/publications/1/')
    assert response.json()['id'] == 1
