from django.contrib.auth.models import User


class Person(User):
    """
    Прокси-модель поверх джанговского пользователя.
    Используется для хранения дополнительных методов.
    """

    class Meta:
        proxy = True
