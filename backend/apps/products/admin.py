from django.contrib import admin

from apps.products.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'updated', 'is_active')
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        (
            None,
            {
                'fields': (
                    'title',
                    'slug',
                    'description',
                    'image',
                    'is_active',
                ),
            },
        ),
    )
