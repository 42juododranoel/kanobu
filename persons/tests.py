from django.contrib.auth.models import User
import pytest

from persons.models import Person


@pytest.fixture
def user():
    return User.objects.create_user(username='test')


@pytest.mark.django_db
def test_person_proxy_model(user):
    person = Person.objects.get(id=user.id)
    assert person.username == user.username
