from dataclasses import dataclass

from apps.core.servises import BaseModelService
from apps.products.models import Category


@dataclass
class CategoryModelService(BaseModelService):
    """Сервис для работы с моделью категории."""


сategories_service = CategoryModelService(Category)
