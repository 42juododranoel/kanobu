from django.contrib.auth.models import User
from freezegun import freeze_time
from mixer.backend.django import mixer
import pytest
from rest_framework.test import APIClient

from comments.models import Comment
from publications.models import Publication


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
