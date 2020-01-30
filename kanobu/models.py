from django.db import models


class BaseModel(models.Model):
    """
    Базовая модель, от которой наследуются остальные модели.
    Нужна для методов, общих для всех моделей.
    """

    class Meta:
        abstract = True

    def update(self, **attributes):
        """
        Обновить свои поля словариком items, потом сохраниться.
        Использовать в тестах, чтобы сократить количество кода.
        """
        for name in attributes:
            setattr(self, name, attributes[name])
        else:
            self.save()
