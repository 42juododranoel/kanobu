import pytest

pytestmark = [pytest.mark.django_db]


def test_list_opinions(api_client, opinion):
    response = api_client.get('/api/opinions/')

    assert response.status_code == 200
    assert response.json()[0]['id'] == opinion.id


def test_retrieve_opinion(api_client, opinion):
    response = api_client.get(f'/api/opinions/{opinion.id}/')

    assert response.status_code == 200
    assert response.json()['id'] == opinion.id


def test_cant_create_opinion_unauthorized(api_client, publication):
    payload = {'category': 0, 'object_id': publication.id, 'content_type': 8}
    response = api_client.post('/api/opinions/', data=payload)

    assert response.status_code == 403


def test_create_opinion_authorized(auth_api_client, publication, person):
    payload = {'category': 0, 'object_id': publication.id, 'content_type': 9, 'owner': person.id}
    response = auth_api_client.post('/api/opinions/', data=payload)

    assert response.status_code == 201
    assert response.json()['id'] == 1


def test_cant_partial_update_opinion_unauthorized(api_client, opinion):
    payload = {'category': opinion.CATEGORY_DISLIKE}
    response = api_client.patch(f'/api/opinions/{opinion.id}/', payload)

    assert response.status_code == 403


def test_partial_update_opinion_authorized(auth_api_client, opinion):
    opinion.update(owner=auth_api_client.user)

    payload = {'category': opinion.CATEGORY_DISLIKE}
    response = auth_api_client.patch(f'/api/opinions/{opinion.id}/', payload)

    assert response.status_code == 200
    assert response.json()['category'] == opinion.CATEGORY_DISLIKE


def test_not_owner_cant_partial_update_opinion(auth_api_client, opinion):
    payload = {'category': opinion.CATEGORY_DISLIKE}
    response = auth_api_client.patch(f'/api/opinions/{opinion.id}/', payload)

    assert response.status_code == 403


def test_cant_update_opinion_unauthorized(api_client, opinion):
    payload = {'category': opinion.CATEGORY_DISLIKE}
    response = api_client.patch(f'/api/opinions/{opinion.id}/', payload)

    assert response.status_code == 403


def test_update_opinion_authorized(auth_api_client, opinion, publication, person):
    opinion.update(owner=auth_api_client.user)

    payload = {'category': opinion.category, 'object_id': publication.id, 'content_type': 9, 'owner': person.id}
    response = auth_api_client.put(f'/api/opinions/{opinion.id}/', payload)

    assert response.status_code == 200
    expected_response_json = payload.copy()
    expected_response_json.update({'id': opinion.id})
    assert response.json() == expected_response_json


def test_not_owner_cant_update_opinion(auth_api_client, opinion):
    payload = {'category': opinion.CATEGORY_DISLIKE}
    response = auth_api_client.patch(f'/api/opinions/{opinion.id}/', payload)

    assert response.status_code == 403


def test_cant_destroy_opinion_unauthorized(api_client, opinion):
    response = api_client.delete(f'/api/opinions/{opinion.id}/')

    assert response.status_code == 403


def test_destroy_opinion_authorized(auth_api_client, opinion):
    opinion.update(owner=auth_api_client.user)

    response = auth_api_client.delete(f'/api/opinions/{opinion.id}/')

    assert response.status_code == 204


def test_not_owner_cant_destroy_opinion(auth_api_client, opinion):
    response = auth_api_client.delete(f'/api/opinions/{opinion.id}/')

    assert response.status_code == 403
