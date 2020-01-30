from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from freezegun import freeze_time
from mixer.backend.django import mixer
import pytest
from rest_framework.test import APIClient

from comments.models import Comment
from publications.models import Publication
from opinions.models import Opinion


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def auth_api_client(api_client, user):
    api_client.force_authenticate(user=user)
    return api_client


@pytest.fixture
def user():
    return User.objects.create_user(username='test')


@pytest.fixture
def person(user):
    return user


@pytest.fixture
def publication():
    with freeze_time('2001-01-01 12:00'):
        return mixer.blend(Publication)


@pytest.fixture
def comment():
    return mixer.blend(Comment)


@pytest.fixture
def opinion():
    return mixer.blend(Opinion)


@pytest.fixture
def opinion_factory():
    def create_opinion(**attributes):
        return mixer.blend(Opinion, **attributes)

    return create_opinion


@pytest.fixture
def publication_opinion():
    return mixer.blend(
        Opinion,
        content_type=ContentType.objects.get_for_model(Publication)
    )


@pytest.fixture
def comment_opinion():
    return mixer.blend(
        Opinion,
        content_type=ContentType.objects.get_for_model(Comment)
    )
