import pytest

pytestmark = [pytest.mark.django_db]


def test_list_comments(api_client, comment):
    response = api_client.get('/api/comments/')
    assert response.status_code == 200
    assert response.json()[0]['id'] == 1


def test_retrieve_comment(api_client, comment):
    response = api_client.get(f'/api/comments/{comment.id}/')
    assert response.status_code == 200
    assert response.json()['id'] == comment.id


def test_cant_create_comment_unauthorized(api_client, person, publication):
    payload = {'text': 'Hello!', 'owner': person.id, 'publication': publication.id}
    response = api_client.post('/api/comments/', data=payload)
    assert response.status_code == 403


def test_create_comment_authorized(auth_api_client, person, publication):
    payload = {'text': 'Hello!', 'owner': person.id, 'publication': publication.id}
    response = auth_api_client.post('/api/comments/', data=payload)
    assert response.status_code == 201
    assert response.json()['id'] == 1
