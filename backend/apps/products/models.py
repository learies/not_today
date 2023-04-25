from django.db import models

from apps.core.models import BaseModel
from apps.products.utils import get_upload_to


class Category(BaseModel):
    """Категории товара."""

    title = models.CharField(
        'Название',
        max_length=256,
        help_text='Добавить название категории не блее 256 символов.',
    )
    slug = models.SlugField(
        'Слаг',
        max_length=256,
        help_text=(
            'Добавить слаг не блее 256 символов. '
            'Слаг должен быть уникальным для каждой категории.'
        ),
    )
    description = models.TextField(
        'Описание',
        blank=True,
        help_text='Добавить описание к категории.',
    )
    image = models.ImageField(
        'Изображение',
        upload_to=get_upload_to,
        blank=True,
        help_text='Добавить изображение к категории.',
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title
