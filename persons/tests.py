import pytest

from persons.models import Person

pytestmark = [pytest.mark.django_db]


def test_person_proxy_model(user):
    person = Person.objects.get(id=user.id)

    assert person.username == user.username
