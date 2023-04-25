from dataclasses import dataclass
from typing import Type, TypeVar

from django.db.models import QuerySet

ModelType = TypeVar("ModelType")


@dataclass
class BaseModelService:
    """Базовый класс для работы с моделями."""

    model: Type[ModelType]

    def get_all(self) -> QuerySet:
        return self.model.objects.all()
