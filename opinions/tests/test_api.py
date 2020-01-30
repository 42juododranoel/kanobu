from django.contrib.contenttypes.models import ContentType
import pytest


@pytest.mark.django_db
def test_list_opinions(api_client, opinion):
    response = api_client.get('/api/opinions/')
    assert response.json()[0]['id'] == 1


@pytest.mark.django_db
def test_retrieve_opinion(api_client, opinion):
    response = api_client.get('/api/opinions/1/')
    assert response.json()['id'] == 1


@pytest.mark.django_db
def test_cant_create_opinion_unauthorized(api_client, publication):
    payload = {'category': 0, 'object_id': publication.id, 'content_type': 8}
    response = api_client.post('/api/opinions/', data=payload)
    assert response.status_code == 403


@pytest.mark.django_db
def test_create_opinion_authorized(auth_api_client, publication):
    payload = {'category': 0, 'object_id': publication.id, 'content_type': 9}
    response = auth_api_client.post('/api/opinions/', data=payload)
    assert response.status_code == 201
