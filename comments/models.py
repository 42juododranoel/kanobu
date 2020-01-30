from django.db import models
from django.utils.translation import ugettext_lazy as _

from kanobu.models import BaseModel
from persons.models import Person
from publications.models import Publication


class Comment(BaseModel):
    """
    Комментарий посетителя сайта.
    """

    text = models.TextField(
        verbose_name=_('Text')
    )
    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        verbose_name=_('Person'),
    )
    publication = models.ForeignKey(
        Publication,
        on_delete=models.CASCADE,
        verbose_name=_('Publication'),
    )
