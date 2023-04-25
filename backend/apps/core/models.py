from django.db import models


class BaseModel(models.Model):
    created = models.DateTimeField(
        'Дата создания',
        auto_now_add=True,
    )
    updated = models.DateTimeField(
        'Дата обновления',
        auto_now=True,
    )
    is_active = models.BooleanField(
        'Активный',
        default=True,
        help_text=(
            'Указывает, что этот объект является активный. '
            'Снять выделение вместо удаления.'
        )
    )

    class Meta:
        abstract = True
