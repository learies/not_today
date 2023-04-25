from typing import Any


def get_upload_to(instance: Any, filename: str) -> str:
    """Возвращает путь, по которому должен быть сохранен загруженный файл.

    Args:
        instance: Экземпляр модели, у которой есть атрибут slug.
        filename: Имя загружаемого файла.

    Returns:
        Строку, которая состоит из объединения строк
        "products/", instance.category.slug, instance.slug и filename.

        Если у instance нет атрибута slug, возникает AttributeError
        который вернёт "products/categories/", instance.slug и filename.
    """

    try:
        return f'products/{instance.category.slug}/{instance.slug}/{filename}'
    except AttributeError:
        return f'products/categories/{instance.slug}/{filename}'
