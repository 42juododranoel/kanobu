from django.db import models
from django.utils.translation import ugettext_lazy as _

from kanobu.models import BaseModel


class Publication(BaseModel):
    """
    Материал на сайте.
    Может быть статьёй или новостью.
    По умолчанию не опубликован.
    """

    CATEGORY_ARTICLE = 0
    CATEGORY_NEWS = 1
    CATEGORIES = (
        (CATEGORY_ARTICLE, _('Article')),
        (CATEGORY_NEWS, _('News')),
    )

    title = models.CharField(
        verbose_name=_('Title'),
        max_length=255,
    )

    content = models.TextField(
        verbose_name=_('Content'),
    )

    author = models.CharField(
        verbose_name=_('Author'),
        max_length=255,
    )

    category = models.SmallIntegerField(
        verbose_name=_('Category'),
        default=CATEGORIES[0][0],
        choices=CATEGORIES,
    )

    created_at = models.DateTimeField(
        verbose_name=_('Created at'),
        auto_now_add=True,
    )

    published_at = models.DateTimeField(
        verbose_name=_('Published at'),
        blank=True,
        null=True,
    )

    @property
    def is_article(self):
        return self.category == self.CATEGORY_ARTICLE

    @property
    def is_news(self):
        return self.category == self.CATEGORY_NEWS
