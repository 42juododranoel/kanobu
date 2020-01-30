from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import ugettext_lazy as _

from kanobu.models import BaseModel


class Opinion(BaseModel):
    """
    Мнение посетителя сайта о материале или комментарии.
    Может быть лайком или дизлайком.

    При создании мнения через АПИ нужно указать:
    - object_id — id материала или комментария;
    - content_type — id джанговского контент-тайпа (8 — publication, 9 — comment).
    """

    CATEGORY_LIKE = 0
    CATEGORY_DISLIKE = 1
    CATEGORIES = (
        (CATEGORY_LIKE, _('Like')),
        (CATEGORY_DISLIKE, _('Dislike')),
    )

    category = models.SmallIntegerField(
        verbose_name=_('Category'),
        default=CATEGORIES[0][0],
        choices=CATEGORIES,
    )

    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    @property
    def is_like(self):
        return self.category == self.CATEGORY_LIKE

    @property
    def is_dislike(self):
        return self.category == self.CATEGORY_DISLIKE
