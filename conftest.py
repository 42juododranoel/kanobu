import pytest
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from freezegun import freeze_time
from mixer.backend.django import mixer

from comments.models import Comment
from kanobu.utils.api_client import UserAPIClient
from opinions.models import Opinion
from publications.models import Publication


@pytest.fixture
def api_client():
    return UserAPIClient()


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
def create_opinion():
    def _create_opinion(**attributes):
        return mixer.blend(Opinion, **attributes)

    return _create_opinion


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
